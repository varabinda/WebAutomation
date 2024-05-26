import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/automation-practice-form"

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)

time.sleep(2)

# radio = driver.find_element(By.ID, "gender-radio-2")
radio = driver.find_element(By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline'][1]")
driver.execute_script("arguments[0].scrollIntoView();", radio)
radio.click()

assert radio.is_selected(), "Gender 'Male' not selected"

time.sleep(10)

driver.quit()