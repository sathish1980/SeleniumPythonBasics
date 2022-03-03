import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class facebookaccnt:
    def method1(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe",options=options)
        driver.maximize_window()

        driver.get("https://en-gb.facebook.com/")
        #driver.find_element_by_xpath("//a[@data-testid='open-registration-form-button']").click()
        createaccountbutton=driver.find_element_by_xpath("//a[@data-testid='open-registration-form-button']")
        createaccountbutton .click()
        #driver.implicitly_wait(10)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "firstname")))
        #time.sleep(2)
        driver.find_element_by_name("firstname").send_keys("sathish kumar")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "lastname")))
        driver.find_element_by_name("lastname").send_keys("kumar")

        time.sleep(2)
    def value(self):
        True
        #driver.find_element_by_name("firstname").send_keys("sathish kumar")
        #driver.find_element_by_name("lastname").send_keys("sathish kumar")
obj1= facebookaccnt()
obj1.method1()