import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

time.sleep(2)

title = driver.find_element(By.XPATH, "//legend/b")
print(f"Title: {title.text}")
if title.text != "COUNTRY":
    print("Title Country not found")
    sys.exit(1)

dropdown = driver.find_element(By.ID, "autosuggest")
dropdown.send_keys("me")

time.sleep(3)

dd_options = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a[@class='ui-corner-all']")
for option in dd_options:
    if option.text == "France Metropolitan":
        option.click()
        break

time.sleep(3)

selection = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert selection == "France Metropolitan" "France Metropolitan not selected"

time.sleep(10)
print("closing driver")
driver.quit()