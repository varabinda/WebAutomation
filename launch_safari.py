from selenium import webdriver as wd
import time

driver = wd.Safari()
driver.maximize_window()
driver.get("https://www.selenium.dev")
time.sleep(15)
print(f"Title: {driver.title}")
print(f"URL: {driver.current_url}")
driver.quit()