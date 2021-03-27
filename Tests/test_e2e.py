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


class Testone(BaseClass):

    def test_e2e(self):

        homepg = Homepage(self.driver)
        chckpg = Checkoutpage(self.driver)

        driver = self.driver
        wait = WebDriverWait(driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@class="btn btn-success"]')))

        submit_button = homepg.success_button()
        if submit_button.is_displayed():
            print("Hello I am There")
        else:
            print("Hello I am Not there")

        homepg.shopitems().click()
        products = chckpg.getCardTitle()

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                #Add item into cart
                product.find_element_by_xpath("div/button").click()

        driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element_by_link_text("India").click()
        driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        driver.find_element_by_css_selector("[type='submit']").click()
        successText = driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        driver.get_screenshot_as_file("screen.png")
