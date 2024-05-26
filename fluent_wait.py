from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec

import time

URL = 'https://www.selenium.dev/selenium/web/dynamic.html'

driver = wd.Chrome()
driver.get(URL)

revealed = driver.find_element(By.ID, "revealed")
is_visible = 'Yes' if revealed.is_displayed() else 'No'
print(f"Is textbox visible? {is_visible}")
driver.find_element(By.ID, "reveal").click()
# revealed.send_keys("Displayed")

errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
wait.until(ec.visibility_of_element_located((By.ID, "revealed")))

revealed.send_keys("Displayed")
assert revealed.get_property("value") == "Displayed", "Text enter is not displayed"

time.sleep(10)


