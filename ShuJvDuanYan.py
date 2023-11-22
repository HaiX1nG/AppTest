from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class assertEqual(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/alertTest.htm')
        self.driver.implicitly_wait(60)

    def test_case(self):
        self.driver.find_element(By.NAME, "b1").click()
        text = self.driver.switch_to.alert.text
        sleep(3)
        self.assertEqual(text, "Alert", msg="测试不通过，弹框信息不同！")
        self.driver.switch_to.alert.accept()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
