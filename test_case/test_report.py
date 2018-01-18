from selenium import webdriver
import unittest
from time import sleep


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        sleep(2)
        title = driver.title
        self.assertEqual(title, 'unittest_百度搜索')
        print(title, '-->test_baidu search success.')

    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(Baidu('test_baidu_search'))
#
#     # 定义报告存放路径
#     testReport = open('./result.html', 'wb')
#     # 定义测试报告
#     runner = HTMLTestRunner(stream=testReport, title='百度搜索测试报告', description='用例执行情况: ')
#     runner.run(testunit)  # 运行测试用例
#     testReport.close()  # 关闭报告文件
if __name__ == '__main__':
    unittest.main()
