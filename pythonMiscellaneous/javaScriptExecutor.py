from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Saving Screenshots
driver.get_screenshot_as_file("C:/Users/smore/PycharmProjects/PythonSelenium/Screenshots/screen1.png")

# JavaScript Execution
driver.execute_script("window.scroll(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("C:/Users/smore/PycharmProjects/PythonSelenium/Screenshots/screen2.png")

print("Headless mode execution completed")
driver.close()
