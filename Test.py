from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
sleep(2)

browser.maximize_window()

element = browser.find_element(By.ID, 'kw')
element.send_keys('学习强国')
sleep(1)

element1 = browser.find_element(By.ID, 'su')
element1.click()
sleep(1)

element2 = browser.find_element(By.PARTIAL_LINK_TEXT, '学习强国')
element2.click()
sleep(3)
browser.switch_to.window(browser.window_handles[-1])
browser.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')
