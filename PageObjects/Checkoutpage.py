from selenium.webdriver.common.by import By


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    def getCardTitle(self):
        return self.driver.find_elements(*Checkoutpage.cardTitle)

