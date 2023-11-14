from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.bilibili.com')
all_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[0])

driver.maximize_window()
sleep(1)

nav_element = driver.find_element(By.CLASS_NAME, "nav-search-input")
nav_element.send_keys("黑马程序员")

btn_element = driver.find_element(By.CLASS_NAME, "nav-search-btn")
btn_element.click()

driver.switch_to.window(driver.window_handles[1])
xpath_element = driver.find_element(By.PARTIAL_LINK_TEXT, '黑马程序员')
xpath_element.click()

driver.switch_to.window(driver.window_handles[2])
xpath_element1 = driver.find_element(By.XPATH, '//*[@id="i-masterpiece"]/div/div[3]/a[1]')
xpath_element1.click()
# xpath_element = driver.find_element(By.XPATH, '//*[@id="local"]/a')
# xpath_element.click()

# driver.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')

# driver.close()
# driver.quit()
