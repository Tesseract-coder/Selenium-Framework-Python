from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import datetime

def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="my option: type1 or chrome"
    )


@pytest.fixture(scope="class")
def Setup(request):

    browser = request.config.getoption("browsername")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    elif browser == 'Edge':
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    elif browser == 'Firefox':
        driver = webdriver.Firefox(executable_path="C:\\gekodriver.exe")

    else:
        print("Something Different Browser")

    print("This is Setup Method and opening Browser")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    print("This is Teardown Method and closing Browser")

