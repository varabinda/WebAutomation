import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

time.sleep(2)

radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
selected_radio_button = None
for radio_button in radio_buttons:
    if radio_button.get_attribute('value') == 'radio3':
        selected_radio_button = radio_button
        radio_button.click()

assert selected_radio_button.is_selected() == True, "Radio3 is not selected"

time.sleep(3)

checkbox_options = driver.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
print(checkbox_options)
selected_checkboxes = []
for checkbox_option in checkbox_options:
    print(checkbox_option.get_attribute("value"))
    if 'option1' == checkbox_option.get_attribute('value') or 'option3' == checkbox_option.get_attribute('value'):
        selected_checkboxes.append(checkbox_option)
        checkbox_option.click()

for checkbox in selected_checkboxes:
    assert checkbox.is_selected() == True, f"Checkbox {checkbox.get_attribute('value')} is not selected"

time.sleep(3)

unselected_checkbox = None
for checkbox in selected_checkboxes:
    if 'option3' == checkbox.get_attribute('value'):
        checkbox.click()
        unselected_checkbox = checkbox

assert unselected_checkbox.is_selected() == False, f"Checkbox {unselected_checkbox.get_attribute('value')} is still checked"

time.sleep(5)