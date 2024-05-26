from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

driver = wd.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")

time.sleep(3)

TITLE_TEXT = "Text Box"
ADDRESS = '''A-143, 9th Floor, Sovereign Corporate Tower
Sector-136, Noida
Uttar Pradesh - 201305
'''

print("Verifying the title")
title_element = driver.find_element(By.CLASS_NAME, "text-center")
assert title_element.text == TITLE_TEXT, f"The title text '{TITLE_TEXT}' not found"

print("Providing full name")
name_element = driver.find_element(By.ID, "userName")
# driver.execute_script("arguments[0].scrollIntoView();", name_element)
name_element.send_keys("John Doe Smith")

time.sleep(3)

print("Providing email")
email_element = driver.find_element(By.ID, "userEmail")
# driver.execute_script("arguments[0].scrollIntoView();", email_element)
email_element.send_keys("john.doe@gmail.com")

time.sleep(3)

print("Providing current address")
current_add_element = driver.find_element(By.ID, "currentAddress")
# driver.execute_script("arguments[0].scrollIntoView();", current_add_element)
current_add_element.send_keys(ADDRESS)

time.sleep(3)

print("Providing permanent address")
permanent_add_element = driver.find_element(By.ID, "permanentAddress")
# driver.execute_script("arguments[0].scrollIntoView();", permanent_add_element)
permanent_add_element.send_keys(ADDRESS)

time.sleep(3)

print("Clicking submit button")
button_element = driver.find_element(By.ID, "submit")
button_element.click()

time.sleep(3)

print("Extracting line 1")
line_1_element = driver.find_element(By.XPATH, "//p[1]")
print(line_1_element.text)

print("Extracting line 2, email")
line_2_element = driver.find_element(By.XPATH, "//p[2]")
print(line_2_element.text)

time.sleep(10)

driver.quit()
