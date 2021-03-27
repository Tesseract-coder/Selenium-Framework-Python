import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/#/index")
driver.implicitly_wait(10)
time.sleep(10)
print(driver.title)
driver.find_element_by_xpath("//li/a[contains(text(),'Articles')]").click()
word = driver.find_element_by_xpath("//span[text()='Selenium']").text
assert "Rahul Shetty Academy Blog – Just another WordPress site" in driver.title
driver.execute_script("document.getElementsByClassName('tve-disabled-text-inner')[3].click")




