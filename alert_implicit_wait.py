import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/alerts"

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(URL)

# Check the title
title = driver.find_element(By.XPATH, "//h1[@class='text-center']")
assert title.text == 'Alerts', "Alerts on page not found"

button = driver.find_element(By.ID, "timerAlertButton")
driver.execute_script("arguments[0].scrollIntoView();", button)
print(button.text)
button.click()

# Switch to the alert
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())

# Get the text of the alert
alert_text = alert.text
print("Alert text:", alert_text)

# Accept the alert (click OK)
alert.accept()

print("closing driver")
driver.quit()