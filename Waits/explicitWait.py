import time

from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

promoMSG = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoMSG)

driver.close()

