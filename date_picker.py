"""
This script automates interaction with the automation practice form page on https://demoqa.com/automation-practice-form using Selenium.

It performs the following steps:
1. Navigates to the specified URL.
2. Maximizes the browser window.
3. Checks if the page title is 'Practice Form'.
4. Selects a date of birth (30th November 1995) using dropdowns for year and month, and a clickable day.
5. Verifies that the selected date is correctly set.
6. Waits for 10 seconds to observe the result.
7. Closes the browser.

Dependencies:
- selenium: To install, run `pip install selenium`
- Chrome WebDriver: Ensure the Chrome WebDriver executable is in your PATH or specify its location.

Usage:
    python date_picker.py
"""

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

# Check if on correct page
title = driver.find_element(by=By.XPATH, value="//h1[@class='text-center']")
if "Practice Form" != title.text:
    print("Title Practice Form not found")
    sys.exit(1)

dob_element = driver.find_element(by=By.ID, value="dateOfBirthInput")
driver.execute_script("arguments[0].scrollIntoView();", dob_element)
dob_element.click()

time.sleep(3)

year_select = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
for year in year_select.options:
    if "1995" == year.text:
        print(f"Selecting year {year.text}")
        year.click()
        break

time.sleep(3)

month_select = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
for month in month_select.options:
    if "November" == month.text:
        print(f"Selecting month {month.text}")
        month.click()
        break

time.sleep(3)

day_element = driver.find_element(By.XPATH, "//div[@aria-label='Choose Thursday, November 30th, 1995']")
day_element.click()

time.sleep(3)
By.P

date = driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
# date = driver.find_element(By.ID, "dateOfBirthInput")
# date = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
selected_date = date.get_attribute('value')
print(f"Date {selected_date}")
if "30 Nov 1995" != selected_date:
    print(f"Date not set to 30 Nov 1995")
    sys.exit(1)

time.sleep(10)
