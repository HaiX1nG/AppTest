from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')
all_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[-1])
id_element = driver.find_element(By.ID, 'kw')
id_element.send_keys('武宝珠')
sleep(1)
id_element1 = driver.find_element(By.ID, 'su')
id_element1.click()
sleep(2)

text_element = driver.find_element(By.PARTIAL_LINK_TEXT, '武宝珠-江西外语外贸职业学院电子商务学院')
text_element.click()
driver.switch_to.window(driver.window_handles[-1])
driver.maximize_window()

driver.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')
