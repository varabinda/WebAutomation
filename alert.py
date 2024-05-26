"""
This script automates interaction with the alerts demo page on https://demoqa.com/alerts using Selenium.

It performs the following steps:
1. Navigates to the specified URL.
2. Maximizes the browser window.
3. Verifies that the page title is 'Alerts'.
4. Clicks a button to trigger a JavaScript alert.
5. Reads the text from the alert.
6. Accepts (closes) the alert.
7. Waits for 25 seconds.
8. Closes the browser.

Dependencies:
- selenium: To install, run `pip install selenium`
- Chrome WebDriver: Ensure the Chrome WebDriver executable is in your PATH or specify its location.

Usage:
    python alert.py
"""

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