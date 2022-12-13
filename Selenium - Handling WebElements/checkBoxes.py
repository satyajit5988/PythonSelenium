from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
CBList = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for CB in CBList:
    if CB.get_attribute("value") == 'option2':
        CB.click()
        assert CB.is_selected()
        break

driver.close()

