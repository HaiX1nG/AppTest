from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.baidu.com')
#
# sleep(2)

# browser.get('http://www.jd.com')
# browser.implicitly_wait(30)
#
# element = browser.find_element(By.XPATH, '//*[@id="key"]')
# element.send_keys('电脑')
#
# element1 = browser.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
# element1.click()
#
# element2 = browser.find_element(By.PARTIAL_LINK_TEXT, '华为笔记本电脑MateBook D 14 SE版')
# element2.click()
#
# browser.switch_to.window(browser.window_handles[-1])
# print(browser.current_url)

WebDriverWait(browser, 20, 0.5).until(lambda e1: browser.find_element(By.ID, 'kw'))
browser.find_element(By.ID, 'kw').send_keys('手机')
browser.find_element(By.ID, 'kw').send_keys(Keys.ENTER)
sleep(2)
browser.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')
