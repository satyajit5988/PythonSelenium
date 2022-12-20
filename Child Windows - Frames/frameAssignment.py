import time

from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".blinkingText")))

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])
Message = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
StrippedM = Message.split()
driver.close()

driver.switch_to.window(windows[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(StrippedM[4])
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("learning")

driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

# time.sleep(2)

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))

error = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text
print(error)

driver.close()
