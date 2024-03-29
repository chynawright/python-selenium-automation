# Amazon Locators

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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(10)

# Amazon logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo' and @role='img' and @aria-label='Amazon']")

# Email Field
driver.find_element(By.XPATH,"//*[@type='email' and @id='ap_email'and @tabindex='1']")

# Continue Button
driver.find_element(By.XPATH, "//input[@id='continue' and @class='a-button-input' and @tabindex='5']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link - my amazon sign in page does not have this button
# Other issues with Sign-In link - my amazon sign in page does not have this button

# Create your Amazon account button
driver.find_element("//span[@id='auth-create-account-link']")

