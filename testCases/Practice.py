from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from time import sleep

# instantiate a new Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# launch URL
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
sleep(1)

driver.find_element(By.ID, 'Email').clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID, 'Password').clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

driver.close()