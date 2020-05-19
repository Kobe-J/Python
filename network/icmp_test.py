import os
import time


def shend_icmp_packet(ip_address,times):
    try:
        response = os.popen('ping'+' '+'-n'+' '+times+' '+ip_address)
        response = response.read()
        # 取出丢包率
        lost = response[response.index("(")+1:response.index("%")+1]
        #取出指定的延时字符串
        # res = list(response)
        # a = 0
        # count = 0
        # for r in res:
        #     count += 1
        #     if r == "=":
        #         a = count
        # print(a)
        response = response[response.index("最短"):]
        print(response)

        # 取出执行的延迟
        i = 0
        j = []
        res1 = list(response)
        for r in res1:
            i += 1
            if r == "s":
                j.append(i)

        min = response[:j[0]-1]
        avg = response[j[0]:j[1]-1]
        max = response[j[1]:j[2]-1]
        return min, avg, max, lost
    except :
        print("ping exec error")
        file = open("icmp_logs.txt","a")
        file.write(time.asctime(time.localtime(time.time())) +" ping exec error \n")