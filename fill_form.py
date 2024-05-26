import sys
import time

import selenium.webdriver as wd
from selenium.webdriver.common.by import By

SITE_URL = "https://demoqa.com/"
NAME='John Doe'
ADDRESS = '''A-143, 9th Floor, Sovereign Corporate Tower
Sector-136, Noida
Uttar Pradesh - 201305
'''

driver = wd.Chrome()
driver.maximize_window()
driver.get(SITE_URL)
print(f"Title: {driver.title}, URL: {driver.current_url}")

# Click on Elements after scrolling
element = driver.find_element(by=By.XPATH, value="//div[@class='card-body' and h5/text()='Elements']/..")
driver.execute_script("arguments[0].scrollIntoView();", element)
if element.is_displayed() and element.is_enabled():
    element.click()

# Check if Elements is visible
dd_element = driver.find_element(by=By.XPATH, value="//div[@class='header-text' and text()='Elements']")
if dd_element.text != 'Elements':
    print("Elements dropdown not found!")
    sys.exit(1)
time.sleep(3)

# find Text box under Elements
tb_textbox = driver.find_element(by=By.XPATH, value="//span[@class='text' and text()='Text Box']/..")
tb_textbox.click()
time.sleep(3)

# check of Text Box title is visible
title = driver.find_element(by=By.XPATH, value="//h1[@class='text-center' and text()='Text Box']")
if title.text != 'Text Box':
    print("Title Text Box not found!")
    sys.exit(1)
time.sleep(3)

full_name_title = driver.find_element(by=By.ID, value='userName-label')
if full_name_title.text != 'Full Name':
    print("Full name label not found!")
    sys.exit(1)

full_name_tb = driver.find_element(by=By.ID, value='userName')
full_name_tb.send_keys(NAME)

email_title = driver.find_element(by=By.ID, value='userEmail-label')
if email_title.text != 'Email':
    print("Email label not found!")
    sys.exit(1)

email_tb = driver.find_element(by=By.ID, value='userEmail')
email_tb.send_keys('john.doe@gmail.com')

time.sleep(3)

cur_add_title = driver.find_element(by=By.ID, value='currentAddress-label')
driver.execute_script("arguments[0].scrollIntoView();", cur_add_title)
if cur_add_title.text != 'Current Address':
    print("Current Address label not found!")
    sys.exit(1)

time.sleep(3)

cur_add_tb = driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Current Address']")
cur_add_tb.send_keys(ADDRESS)

perm_add_title = driver.find_element(by=By.XPATH, value="//label[@class='form-label' and text()='Permanent Address']")
if perm_add_title.text != 'Permanent Address':
    print("Permanent Address label not found!")
    sys.exit(1)

perm_add_tb = driver.find_element(by=By.ID, value="permanentAddress")
perm_add_tb.send_keys(ADDRESS)

time.sleep(5)
submit_button = driver.find_element(by=By.ID, value="submit")
submit_button.click()

name_op = driver.find_element(by=By.ID, value='name')
if 'John Doe' not in name_op.text:
    print("Name not found!")
    sys.exit(1)

time.sleep(5)

print('Closing driver')
driver.quit()
