import time

from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
name = 'Goldy'

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

time.sleep(3)

alert = driver.switch_to.alert
PopUpText = alert.text
# print(PopUpText)

assert name in PopUpText
alert.accept()
# alert.dismiss()
print("First Alert Done")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()

alert = driver.switch_to.alert
PopUpText1 = alert.text
# print(PopUpText1)

assert name in PopUpText1
alert.dismiss()
print("Second Alert Done")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()

alert = driver.switch_to.alert
alert.accept()
print("Third Alert Done")

driver.close()

