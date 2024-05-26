import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

URL = "https://demoqa.com/alerts"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

time.sleep(2)

# Check the title
title = driver.find_element(By.XPATH, "//h1[@class='text-center']")
assert title.text == 'Alerts', "Alerts on page not found"

driver.find_element(By.ID, "alertButton").click()
time.sleep(2)

# Switch to the alert
alert = Alert(driver)

# Get the text of the alert
alert_text = alert.text
print("Alert text:", alert_text)

# Accept the alert (click OK)
alert.accept()

time.sleep(25)
print("closing driver")
driver.quit()