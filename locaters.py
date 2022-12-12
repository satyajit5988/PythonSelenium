from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, Name, Linktext

# CSSName
# tag-name[attribute='value']  --> input[name='name']
# .classname --> .alert-success / #ID --> #inlineRadio1

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Goldy")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abc123")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath
# //tag-name[@attribute='value']  --> //input[@type='submit']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

