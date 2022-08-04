

from pageObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.implicitly_wait(5)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.implicitly_wait(5)
            self.lp.clickLogout()
            # self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshots//"+"test_login.png")
            self.driver.close()
            assert False
