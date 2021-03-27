from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import datetime
@pytest.mark.usefixtures("Setup")
class BaseClass:

    def getXpath(self, mainpath, *argument):
        dollars = ['$$1', '$$2', '$$3', '$$4', '$$5']
        for i in range(len(argument)):
            mainpath = mainpath.replace(dollars[i], argument[i])
        return mainpath

    def wait_element(self, driver, element):
        wait = WebDriverWait(driver, 8)
        wait.until(expected_conditions.presence_of_element_located((element)))

    def select_dropdown(self, driver, field, value):
        self.wait_element(driver,field)
        sel = Select(driver.find_element(*field))
        sel.select_by_visible_text(value)
