# code: UTF-8
from appium import webdriver
from time import sleep
import unittest


class appuium_demo(unittest.TestCase):

    def setUp(self):
        self.desired_caps = {'platformName': 'Android', 'platformVersion': '9', 'deviceName': 'CLB0218523001219'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.desired_caps['noReset'] = 'true'

    def test_click(self):
        el1 = self.driver.find_element_by_accessibility_id("火箭猫单词")
        el1.click()
        sleep(3)
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText[1]")
        el2.send_keys("18045647975")
        sleep(3)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView")
        el3.click()
        sleep(3)
        el4 = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc=\"Go back\"]/android.view.ViewGroup/android.widget.ImageView")
        el4.click()

    def tearDown(self):
        sleep(3)
        self.driver.back()
