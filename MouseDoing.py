from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# 获取网址
browser.get('https://www.baidu.com')
sleep(2)
# 全屏
browser.maximize_window()
# # 定位地图
# element = browser.find_element(By.XPATH, '//*[@id="s-top-left"]/a[3]')
# # 模拟鼠标右键
# ActionChains(browser).context_click(element).perform()
# # 定位到设置
# element1 = browser.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
# # 移动鼠标到设置
# ActionChains(browser).move_to_element(element1).perform()
# # 定位到高级搜索
# element2 = browser.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span')
# # 单击高级搜索
# element2.click()
# sleep(1)
# element3 = browser.find_element(By.PARTIAL_LINK_TEXT, '为亚太稳定繁荣作出更多贡献')
# element4 = browser.find_element(By.ID, 'kw')
# ActionChains(browser).drag_and_drop(element3, element4).perform()

browser.find_element(By.ID, 'kw').send_keys('来自风平浪静的明天')

browser.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'c')
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'v')
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.BACK_SPACE*9)
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'v')
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.SPACE*5)
sleep(1)

browser.find_element(By.ID, 'kw').send_keys(Keys.ENTER)
sleep(1)

# 截图
browser.get_screenshot_as_file('C:/Users/Administrator/Desktop/png/testDemo.png')
