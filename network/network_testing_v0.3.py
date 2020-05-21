from network.http_test import *
from network.icmp_test import *
from network.config import *
import threading
import time
import json

http_status = True


def start_check_http(url, title):
    global http_status
    while True:
        if check_http(url, title):
            # http_status = True
            print("http_status :", http_status)
        else:
            http_status = False
            print("http_status :", http_status)
            file = open("http_logs.txt", "a")
            file.write(time.asctime(time.localtime(time.time())) + " : http status is " + str(http_status) + "\n")
        time.sleep(1)


def check_continuous():
    url, title, ip_address, times, domain, dnsserver = analyze_config()
    t_http = threading.Thread(target=start_check_http, args=(url, title))
    t_http.start()


def icmp_continuous():
    global http_status
    global avg_list
    global lost_list

    avg_list = []
    lost_list = []
    url, title, ip_address, times, domain, dnsserver = analyze_config()

    while True:
        if http_status:
            min, avg, max, lost = "", "", "", ""
            try:
                min, avg, max, lost = shend_icmp_packet(ip_address, times)

                avg_flag = 0
                avg_list.append(float(avg))
                for a in avg_list:
                    avg_flag = avg_flag + a
                avg_flag = avg_flag / len(avg_list)

                lost_flag = 0
                lost_list.append(float(lost))
                for b in lost_list:
                    lost_flag = lost_flag + b
                lost_flag = lost_flag / len(lost_list)

                file = open("result.json")
                content = file.read()
                file.close()
                content = json.loads(content)
                content["ping"]["min"] = float(content["ping"]["min"]) if float(content["ping"]["min"]) <= float(
                    min) else float(min)
                content["ping"]["avg"] = avg_flag
                content["ping"]["max"] = float(content["ping"]["max"]) if float(content["ping"]["max"]) >= float(
                    max) else float(max)
                content["ping"]["lost"] = lost_flag
                content = json.dumps(content)

                file = open("result.json", "w")
                file.write(content)
                file.close()
                print('最小延迟：'+min, '平均延迟：'+avg, '最大延迟：'+max, '丢包率：' + lost+'%')
            except:
                pass
        else:
            time.sleep(1)
            continue
        time.sleep(5)


def main():
    c_check = threading.Thread(target=check_continuous)
    i_icmp = threading.Thread(target=icmp_continuous)

    c_check.start()
    i_icmp.start()


if __name__ == '__main__':
    main()
