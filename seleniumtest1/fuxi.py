import unittest
from time import sleep

from selenium import webdriver

# import requests
#
# print(requests.get("http://www.taobao.com").text)

class test(unittest.TestCase):
    def test1(self):
        '''复习一'''
        self.wb = webdriver.Chrome(r'E:\PyCharm 2019.3.3\bin\chromedriver.exe')
        self.wb.get("http://www.baidu.com")
        sleep(3)
        ele = self.wb.find_elements_by_class_name("mnav c-font-normal c-color-t")
        print(ele.text)
        sleep(2)
        self.wb.quit()

