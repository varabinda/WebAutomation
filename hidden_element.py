import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

time.sleep(2)

show = driver.find_element(By.ID, "show-textbox")
hide = driver.find_element(By.ID, "hide-textbox")
driver.execute_script("arguments[0].scrollIntoView();", hide)

textbox = driver.find_element(By.ID, "displayed-text")
# Check if widget is visible
assert textbox.is_displayed(), 'Textbox is visible'

time.sleep(3)

# Hide the textbox
hide.click()

time.sleep(3)

# Check if widget is not visible
assert textbox.is_displayed() == False, 'Textbox is visible'

# Show the textbox
show.click()

# Check if widget is visible
assert textbox.is_displayed(), 'Textbox is not visible'

time.sleep(5)

driver.quit()
