import autoit
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

driver.get("https://www.youtube.com/")
driver.implicitly_wait(10)
time.sleep(10)
print(driver.title)
driver.find_element_by_xpath("//button[contains(text(),'Upload Image')]").click()

autoit.win_wait_active("Open",5)
# autoit.win_wait_active("[CLASS:DirectUIHWND; INSTANCE:2]", 10)
time.sleep(2)
autoit.control_send("Open","[CLASS:Edit; INSTANCE:1]","D:\TCS docs\IMG_9211.JPG")
time.sleep(2)
autoit.control_click("Open","[CLASS:Button; INSTANCE:1]")

time.sleep(10)

driver.find_element_by_xpath("//input[@id='search']").send_keys("Hello")
driver.find_element_by_xpath("//button[@id='search-icon-legacy']").click()
time.sleep(5)
driver.back()
# js = "document.getElementsByClassName('ytd-searchbox')[2].value='Kunal'"
# driver.execute_script(js)
# time.sleep(10)

