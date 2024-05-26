from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
import time

service = Service("./drivers/chromedriver.exe")

driver = wd.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.selenium.dev")
time.sleep(50)
driver.quit()

