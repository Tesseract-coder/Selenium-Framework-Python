from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import datetime

from PageObjects.Checkoutpage import Checkoutpage
from PageObjects.Homepage import Homepage
from Utilities.BaseClass import BaseClass

class TestHome(BaseClass):

    def test_AddUser(self):

        h1 = Homepage(self.driver)
        driver = self.driver

        self.wait_element(driver,Homepage.name)
        h1.get_name_Text().send_keys("Kunal")
        h1.get_email_Text().send_keys("kunalnevrekar2020@gmail.com")
        h1.enter_password().send_keys("Fifa2@11")
        h1.get_Employment_status("Employed")
        h1.Get_DOB().send_keys("03/28/1996")
        self.select_dropdown(driver,h1.gender,"Female")
        h1.success_button().click()
        self.wait_element(driver,Homepage.message)
        Final_Message = h1.get_message().text

        assert "Success!" in Final_Message










