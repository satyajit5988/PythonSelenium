from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service

# Chrome Options
from selenium.webdriver.common.by import By

browserSortedVeggies = []

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Collect all veggie names
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# sort this browser sorted veggies list

browserSortedVeggies.sort()

# Compare both list

assert originalBrowserSortedList == browserSortedVeggies
print("Web Table Is Sorted")

driver.close()

