import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

time.sleep(2)

radio2_element = driver.find_element(by=By.XPATH, value="//input[@value='radio2']")
radio2_element.click()

time.sleep(3)

checkbox_1_element = driver.find_element(by=By.CSS_SELECTOR, value="#checkBoxOption1")
checkbox_1_element.click()

checkbox_3_element = driver.find_element(by=By.CSS_SELECTOR, value="#checkBoxOption3")
checkbox_3_element.click()

time.sleep(10)

driver.quit()