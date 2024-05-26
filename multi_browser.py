import sys
import os
from selenium import webdriver

DRIVER_PATH = './drivers'


def launch_chrome(launch_server):
    driver_path = os.path.join(DRIVER_PATH, 'chromedriver')
    # driver_path <- ./drivers/chromedriver
    print(f"Driver path: {driver_path}")
    if launch_server.lower() == 'yes':
        return webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path))
    else:
        return webdriver.Chrome()


def launch_firefox(launch_server):
    driver_path = os.path.join(DRIVER_PATH, 'geckodriver')
    if launch_server.lower() == 'yes':
        return webdriver.Firefox(service=webdriver.firefox.service.Service(driver_path))
    else:
        return webdriver.Firefox()


def launch_safari(launch_server):
    return webdriver.Safari()


def launch_edge(launch_server):
    driver_path = os.path.join(DRIVER_PATH, 'msedgedriver')
    if launch_server.lower() == 'yes':
        return webdriver.Edge(service=webdriver.edge.service.Service(driver_path))
    else:
        return webdriver.Edge()


def check_title_and_url(driver, expected_title, expected_url):
    actual_title = driver.title
    actual_url = driver.current_url
    if actual_title == expected_title and actual_url == expected_url:
        print("Test Passed! Title and URL match the expected values.")
    else:
        print(f"Test Failed! Expected title: {expected_title}, Actual title: {actual_title}")
        print(f"Expected URL: {expected_url}, Actual URL: {actual_url}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <browser_name> <launch_server>")
        sys.exit(1)

    browser_name = sys.argv[1]
    launch_server = sys.argv[2]

    if browser_name.lower() == 'chrome':
        driver = launch_chrome(launch_server)
    elif browser_name.lower() == 'firefox':
        driver = launch_firefox(launch_server)
    elif browser_name.lower() == 'safari':
        driver = launch_safari(launch_server)
    elif browser_name.lower() == 'edge':
        driver = launch_edge(launch_server)
    else:
        print("Invalid browser name. Supported browsers are Chrome, Firefox, Safari, and Edge.")
        sys.exit(1)

    driver.get('https://www.selenium.dev/')
    check_title_and_url(driver, "Selenium", "https://www.selenium.dev/")
    driver.quit()


main()
