import time

from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

RBList = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
RBList[1].click()

time.sleep(5)

for RB in RBList:
    if RB.get_attribute("value") == 'radio3':
        RB.click()
        assert RB.is_selected()
        break

# To verify if an element is displayed or not on UI

displayElement = driver.find_element(By.ID, "displayed-text")
assert displayElement.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not displayElement.is_displayed()



