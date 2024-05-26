from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import sys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

title = driver.find_element(by=By.XPATH, value="//h1[@class='text-center']")
if "Practice Form" != title.text:
    print("Title text 'Practice Form' not found")
    sys.exit(1)

time.sleep(3)

dob_element = driver.find_element(by=By.ID, value='dateOfBirthInput')
driver.execute_script("arguments[0].scrollIntoView();", dob_element)
dob_element.click()

time.sleep(3)

year_element = driver.find_element(by=By.XPATH, value="//select[@class='react-datepicker__year-select']")
year_select = Select(year_element)
for year in year_select.options:
    if '1995' == year.text:
        print(f"Selecting year {year.text}")
        year.click()
        break

time.sleep(3)

month_element = driver.find_element(by=By.XPATH, value="//select[@class='react-datepicker__month-select']")
month_select = Select(month_element)
for month in month_select.options:
    if month.text == 'November':
        print(f"Selecting month {month.text}")
        month.click()

time.sleep(3)

day_element = driver.find_element(by=By.XPATH, value="//div[@aria-label='Choose Tuesday, November 7th, 1995']")
day_element.click()

time.sleep(3)

date = driver.find_element(By.ID, "dateOfBirthInput")
selected_date = date.get_attribute('value')
print(f"Date {selected_date}")
if "07 Nov 1995" != selected_date:
    print(f"Date not set to 07 Nov 1995")
    sys.exit(1)

time.sleep(10)

driver.quit()