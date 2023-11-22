import csv
import unittest
from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_csv_data(csv_path):
    rows = []
    # 修改文件编码为utf-8解决文件编码报错的问题
    with open(str(csv_path), encoding='utf-8') as csv_data:
        content = csv.reader(csv_data)
        for row in content:
            print(row)
            rows.append(row)
    return rows


@ddt
class TestCase1(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)

    @data(*get_csv_data('MultipleCredentialDriven.csv'))
    @unpack
    def test_search(self, search_value):
        driver = self.driver
        driver.get('https://www.baidu.com')
        input_elem = driver.find_element(By.ID, 'kw')
        input_elem.send_keys(search_value)
        input_elem.submit()
        sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
