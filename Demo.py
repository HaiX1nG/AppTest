from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.jxcfs.com/')
driver.maximize_window()
sleep(1)
js = 'var q = document.documentElement.scrollTop=10000'
driver.execute_script(js)

element = driver.find_element(By.XPATH, '//*[@id="select1"]')
sleep(1)
Select(element).select_by_index(1)
