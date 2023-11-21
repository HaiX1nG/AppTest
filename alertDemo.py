from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("http://sahitest.com/demo/confirmTest.htm")
# element = driver.find_element(By.NAME, 'b1')
# element.click()
# sleep(1)
# confirm = driver.switch_to.alert
# print(confirm.text)
# sleep(1)
# confirm.dismiss()
# sleep(1)
# driver.quit()


# sleep(1)
#
# element = driver.find_element(By.NAME, 'b1')
# element.click()
# sleep(1)
#
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# sleep(2)
# driver.quit()
driver.get("d:\py\下拉框测试.html")
element = driver.find_element(By.ID, 'section1')

Select(element).select_by_value('软件技术')
sleep(1)
Select(element).select_by_index(3)
sleep(1)
Select(element).select_by_visible_text('大数据技术专业')
sleep(1)

for select in Select(element).options:
    print(select.text)
print("===========")

for select in Select(element).all_selected_options:
    print(select.text)
print("===========")

print(Select(element).first_selected_option.text)
sleep(2)
