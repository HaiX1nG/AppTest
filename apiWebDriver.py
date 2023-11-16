from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

title = driver.title
print('当前页面的标题是：{}'.format(title))

url = driver.current_url
print('当前页面的url是：{}'.format(url))

name = driver.name
print('当前浏览器的名称是：{}'.format(name))

source_code = driver.page_source
with open('baidu_sourcecode.txt', 'w', encoding='utf-8') as f:
    f.write(source_code)

window = driver.current_window_handle
print('当前窗口句柄：'+window)

element = driver.find_element(By.LINK_TEXT, '地图')
element.click()
windows = driver.window_handles
print(windows)

driver.switch_to.window(windows[-1])
window = driver.current_window_handle
print('当前窗口句柄：'+window)
