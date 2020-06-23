import os
import time
import request
import datetime


def auto_connect(wifi="NebulAI", alternate=5, timeout=5, testURL="https://www.baidu.com"):
    cmd = "netsh wlan connect name={}".format(wifi)
    flag = False
    while True:
        try:
            request.get(testURL)
            if flag:
                print("重新连接成功！")
                flag = False
            print("连接良好！当前时间{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            time.sleep(alternate)
            return True
        except:
            print("连接错误，正在重新连接...")
            os.popen(cmd)
            time.sleep(timeout)
            flag = True
