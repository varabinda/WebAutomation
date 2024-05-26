from selenium import webdriver
options = webdriver.ChromeOptions()


options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

driver.get("http://www.google.com")
driver.quit()