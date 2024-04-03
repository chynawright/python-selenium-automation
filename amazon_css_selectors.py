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
driver.get('https://www.amazon.com/ap/register?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Freport%2Finfringement&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_noticeform_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon Logo Image
driver.find_element(By.CSS_SELECTOR, "i.a-icon-logo")

# Create Account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Your name field
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

# Email field
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# Password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

# Password requirements text
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

# Create your Amazon Account Button
driver.find_element(By.CSS_SELECTOR, "input#continue")

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy']")

# Sign in (Existing Account)
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")
