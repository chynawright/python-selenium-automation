from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ids
driver.find_element(By.ID, 'twotabsearchbox')

# By xpath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

# by multiple attributes
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @type='text' and @name='field-keywords']")

# practice
driver.find_element(By.XPATH, "//select[@riadescribedby='searchDropdowndescription']")

# searching for text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# searching for text and other attributes
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a ']")
driver.find_element(By.XPATH, "//a[@class='nav-a ' and text()='Best Sellers']")

# any tag + by text and attributes
driver.find_element(By.XPATH, "//*[@class='")

# contains()
driver.find_element(By.XPATH, )