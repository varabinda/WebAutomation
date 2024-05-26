from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import time

URL = "https://rahulshettyacademy.com/seleniumPractise/"
DELAY_SEC = 10

driver = wd.Chrome()
driver.maximize_window()
driver.get(URL)

start = int(time() * 1000)

search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
search_box.send_keys("be")

product_list = driver.find_elements(By.XPATH, "//div[@class='product']")
assert len(product_list) > 0, "No product found"

for product in product_list:
    product_name = product.find_element(By.XPATH, "h4").text
    product_price = product.find_element(By.XPATH, "p").text
    print(product_name, product_price)
    product.find_element(By.XPATH, "div[3]").click()


cart_button = driver.find_element(By.XPATH, "//img[@alt='Cart']")
cart_button.click()

p2c_button = driver.find_element(By.XPATH, "//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']")
p2c_button.click()

promo_textbox = WebDriverWait(driver, DELAY_SEC).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.promoCode')))
promo_textbox.send_keys('rahulshettyacademy')

apply_button = driver.find_element(By.CSS_SELECTOR, ".promoBtn")
apply_button.click()

promo_text = WebDriverWait(driver, DELAY_SEC).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
assert promo_text.text == "Code applied ..!", "Promo not applied"

driver.quit()

end = int(time() * 1000)

print(f"Time taken: {end -start} ms")


