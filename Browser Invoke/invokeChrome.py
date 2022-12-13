from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.google.com")

PageTitle = driver.title
print(PageTitle)
print(driver.current_url)

driver.get("https://www.google.com/images")
driver.back()
driver.refresh()
driver.forward()

driver.close()

