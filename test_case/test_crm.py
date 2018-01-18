from selenium import webdriver
import unittest
from time import sleep


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://crm.xiaowangmao.com'

    def test_crm(self):
        driver = self.driver
        driver.get(self.base_url + '/logout.html')
        driver.find_element_by_xpath('//*[@id="email"]').clear()
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('android4google@163.com')
        driver.find_element_by_xpath('//*[@id="pwd"]').clear()
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('111111')
        driver.find_element_by_id('loginBtn').click()
        sleep(2)
        title = driver.title
        self.assertEqual(title, '小旺猫客服系统')
        print('test_crm login success.')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
