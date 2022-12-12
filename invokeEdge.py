from selenium import webdriver

# Edge Driver
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/smore/PycharmProjects/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

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

