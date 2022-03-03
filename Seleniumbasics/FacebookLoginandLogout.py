
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class facebookloginandlogout:
    def login(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe", options=options)
        driver.maximize_window()
        driver.get("https://en-gb.facebook.com/")
        username = driver.find_element_by_id("email")
        username.send_keys("kumar.sathish189@gmail.com")
        paswword = driver.find_element_by_name("pass")
        paswword.send_keys("Admin@123")
        driver.find_element_by_name("login").click()
        WebDriverWait(driver, 60).until(
           EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Account']//*[name()='svg']")))
        driver.find_element_by_xpath("//div[@aria-label='Account']//*[name()='svg']").click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']")))
        driver.find_element_by_xpath("//span[text()='Log Out']").click()

obj1= facebookloginandlogout()
obj1.login()

