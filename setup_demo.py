# Chrome version: 123.0.6312.87

from selenium import webdriver as wd
import time

driver = wd.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev")
time.sleep(5)
driver.quit()