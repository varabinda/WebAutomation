import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

# Check if on correct page
title = driver.find_element(by=By.XPATH, value="//h1[@class='text-center']")
if "Web Tables" != title.text:
    print("Title Web Tables not found")
    sys.exit(1)

# Dropdown selection
row_count = driver.find_element(by=By.XPATH, value="//select[@aria-label='rows per page']")
driver.execute_script("arguments[0].scrollIntoView();", row_count)
time.sleep(3)
dropdown = Select(row_count)
row_list = dropdown.options.copy()
for row in row_list:
    print(row.text)
    if row.text == "100 rows":
        print(f"Selecting {row.text}")
        row.click()
        break

time.sleep(20)
driver.quit()
