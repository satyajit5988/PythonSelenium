from selenium import webdriver

# Chrome Driver
# from selenium.webdriver.chrome.service import Service

# service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# Firefox Driver
# https://stackoverflow.com/questions/65318382/expected-browser-binary-location-but-unable-to-find-binary-in-default-location
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
#
# options = Options()
# options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
#
# service_obj = Service("C:/Users/smore/PycharmProjects/geckodriver-v0.32.0-win32/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj, options=options)

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

