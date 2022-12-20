from selenium import webdriver

# Chrome Driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/smore/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# hover
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# right click
action.context_click(driver.find_element(By.LINK_TEXT,  "Top")).perform()

# move to element
action.context_click(driver.find_element(By.LINK_TEXT,  "Reload")).click().perform()

print(driver.current_url)

driver.close()