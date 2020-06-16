import unittest

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


class unittest_demo1(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.qq.com'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)# 隐性等待30秒
        self.driver.get(self.url)
        self.driver.find_element_by_xpath("//*[@id='top-login']/div[3]/a").click()
        sleep(2)
        self.driver.switch_to.frame("ptlogin_iframe")
        sleep(2)
        self.driver.find_element_by_id("switcher_plogin").click()
        sleep(2)

    def login(self, username, passwrod):
        self.driver.find_element_by_id('u').send_keys(username)
        sleep(2)
        self.driver.find_element_by_id('p').send_keys(passwrod)
        sleep(2)
        self.driver.find_element_by_id('login_button').click()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_loginsSuccess(self):
        '''登录异常'''
        self.login("1348315884", '12300..')
        sleep(2)
        button = self.driver.find_element_by_id('tcaptcha_drag_thumb')
        sleep(2)
        action = ActionChains(self.driver)
        action.click_and_hold(button).perform()
        action.reset_actions()
        action.move_by_offset(180, 0).perform()
        tip = self.driver.find_element_by_css_selector("#qlogin_tips_2 > a").text
        sleep(3)
        print(tip)
        self.assertEqual(tip, 'QQ手机版')

    def test_nulluser(self):
        """用户名为空"""
        self.login('', '', '')
        sleep(3)
        self.driver.switch_to.alert().accept()
        sleep(3)
        nullusererror = self.driver.switch_to.alert().text
        sleep(3)
        self.assertEqual(nullusererror, '请输入管理员账号')

    def test_nullpwd(self):
        """密码为空"""
        self.login('13620180611', '', '')
        sleep(3)
        self.driver.switch_to.alert().accept()
        sleep(3)
        nullpassword = self.driver.switch_to.alert().text
        sleep(3)
        self.assertEqual(nullpassword, '请输入管理员密码')

    def test_nulltxtVerify(self):
        """验证码为空"""
        self.login('13620180611', 'Aa654321', '')
        sleep(3)
        self.driver.switch_to.alert().accept()
        sleep(3)
        nulltxtVerify = self.driver.switch_to.alert().text
        sleep(3)
        self.assertEqual(nulltxtVerify, '请输入验证码')

    if __name__ == '__main__':
        unittest.main()
