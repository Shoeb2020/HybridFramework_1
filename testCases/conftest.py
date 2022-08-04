from pageObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
