from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('http://192.168.70.9/ceshi/front/login.do')

all_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[-1])

driver.maximize_window()
sleep(1)

id_element = driver.find_element(By.ID, 'loginName')
id_element.send_keys('322030822')
sleep(1)

id_element2 = driver.find_element(By.ID, 'pwd')
id_element2.send_keys('322030822')
sleep(1)

xpath_element = driver.find_element(By.XPATH, '//*[@id="fmedit"]/div/div[5]/input')
xpath_element.click()
sleep(1)

xpath_element1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/table/tbody/tr[2]/td[2]/div/a')
xpath_element1.click()
sleep(1)


xpath_element2 = driver.find_element(By.XPATH, '//*[@id="cboxLoadedContent"]/div/div/div[2]/div[6]/div[2]/a')
xpath_element2.click()
sleep(1)

driver.switch_to.window(driver.window_handles[1])
id_element3 = driver.find_element(By.ID, 'taskId')
id_element3.send_keys('222')
sleep(1)

id_element4 = driver.find_element(By.ID, 'loginName')
id_element4.send_keys('322030822')
sleep(1)

id_element5 = driver.find_element(By.ID, 'password')
id_element5.send_keys('xuhaixing123')
sleep(1)

id_element6 = driver.find_element(By.ID, 'vericode')
id_element6.send_keys('shtd')
sleep(1)

xpath_element3 = driver.find_element(By.XPATH, '//*[@id="fmedit"]/div[2]/div[6]/input')
xpath_element3.click()
sleep(1)

driver.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')
