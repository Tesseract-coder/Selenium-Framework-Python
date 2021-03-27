from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Homepage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    successbutton = (By.XPATH, '//input[@class="btn btn-success"]')
    name = (By.XPATH, "//input[@name='name' and contains(@class,'form-control')]")
    email = (By.XPATH, "//input[@name='email' and contains(@class,'form-control')]")
    password = (By.ID, 'exampleInputPassword1')
    gender = (By.ID, 'exampleFormControlSelect1')
    Employment_status = (By.XPATH, "//label[text()='Employment Status: ']//following::label[text()='$$1']")
    DOB = (By.XPATH, "//input[@type='date']")
    message = (By.XPATH, "//div[contains(@class,'success')]")

    def get_message(self):
        return self.driver.find_element(*Homepage.message)

    def shopitems(self):
        return self.driver.find_element(*Homepage.shop)

    def Get_DOB(self):
        return self.driver.find_element(*Homepage.DOB)

    def success_button(self):
        return self.driver.find_element(*Homepage.successbutton)

    def get_name_Text(self):
        return self.driver.find_element(*Homepage.name)

    def get_email_Text(self):
        return self.driver.find_element(*Homepage.email)

    def enter_password(self):
        return self.driver.find_element(*Homepage.password)

    def get_Gender(self):
        return self.driver.find_element(*Homepage.gender)

    def get_Employment_status(self, value):
        finalpath = self.getXpath(Homepage.Employment_status[1], value)
        return self.driver.find_element(Homepage.Employment_status[0],finalpath)

