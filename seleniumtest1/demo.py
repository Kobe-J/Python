from time import sleep

from selenium import webdriver

wb = webdriver.Chrome()
wb.get("http://www.baidu.com")
print(wb.find_element_by_id("s-top-left").text)
sleep(2)
wb.quit()