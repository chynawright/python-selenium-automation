from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@aria-expanded='false' and @aria-label='Account, sign in' and @data-test='@web/AccountLink']").click()

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(4)


actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert 'Sign into your Target account' in actual_text, f'Error! Text coffee not in {actual_text}'

driver.find_element(By.XPATH, "//button[@type='submit' and @id='login']")

