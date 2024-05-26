import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

URL = "https://demoqa.com/alerts"

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)

time.sleep(2)

title = driver.find_element(By.XPATH, "//h1[@class='text-center']")
assert title.text == 'Alerts', "Alerts on page not found"

button = driver.find_element(By.ID, "promtButton")
driver.execute_script("arguments[0].scrollIntoView();", button)
button.click()

# Switch to the alert
alert = Alert(driver)

# Get the text of the alert
prompt_text = alert.text
print("Prompt text:", prompt_text)

prompt_input = "Alice Dominique"
alert.send_keys(prompt_input)

time.sleep(3)
alert.accept()

time.sleep(2)

prompt_result = driver.find_element(By.ID, "promptResult")
assert prompt_input in prompt_result.text, "Entered text not found"

print("closing driver")
driver.quit()