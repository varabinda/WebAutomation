"""
This script automates interaction with the automation practice form page on https://demoqa.com/automation-practice-form using Selenium.

It performs the following steps:
1. Navigates to the specified URL.
2. Maximizes the browser window.
3. Waits for the page to load.
4. Selects the first radio button for gender.
5. Asserts that the radio button is selected.
6. Waits for 10 seconds to observe the result.
7. Closes the browser.

Dependencies:
- selenium: To install, run `pip install selenium`
- Chrome WebDriver: Ensure the Chrome WebDriver executable is in your PATH or specify its location.

Usage:
    python click_radio.py
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/automation-practice-form"

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)

time.sleep(2)

# radio = driver.find_element(By.ID, "gender-radio-2")
radio = driver.find_element(By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline'][1]")
driver.execute_script("arguments[0].scrollIntoView();", radio)
radio.click()

assert radio.is_selected(), "Gender 'Male' not selected"

time.sleep(10)

driver.quit()
