from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

selenium_service = Service("./drivers/chromedriver")

driver = wd.Chrome(service=selenium_service)
driver.maximize_window()
driver.get("https://demoqa.com")
print(f"Title: {driver.title}, URL: {driver.current_url}")

header = driver.find_element(by=By.XPATH, value="//div[@class='card-body' and h5/text()='Elements']/..")
driver.execute_script("arguments[0].scrollIntoView();", header)
if header.is_displayed() and header.is_enabled():
    header.click()
time.sleep(2)

element = driver.find_element(by=By.XPATH , value="//span[@class='text' and text()='Text Box']/..")
element.click()

user_name = driver.find_element(by=By.CSS_SELECTOR, value="input[placeholder='Full Name'][id='userName']")
user_name.send_keys("test-007")



time.sleep(5)
driver.quit()