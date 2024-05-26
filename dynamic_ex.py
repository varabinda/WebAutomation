import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver = wd.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

button_1_element = driver.find_element(By.ID, "reveal")
button_1_element.click()

textbox_element = driver.find_element(By.ID, "revealed")
time.sleep(2)

assert textbox_element.is_displayed(), "The textbox is invisible"
textbox_element.send_keys("Displayed")

print(f"Text is {textbox_element.text}")



time.sleep(5)
