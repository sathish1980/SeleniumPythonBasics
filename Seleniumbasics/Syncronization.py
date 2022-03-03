
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sync:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def sync1(self):
        self.driver.get("https://en-gb.facebook.com/")
        self.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
       # self.driver.implicitly_wait(60)
        element = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.NAME,"firstname")))
        self.driver.find_element_by_name("firstname").send_keys("918279889")
        self.driver.find_element_by_name("lastname").send_keys("918279889")
        self.driver.find_element_by_name("reg_email__").send_keys("918279889")
        self.driver.find_element_by_name("reg_passwd__").send_keys("918279889")

obj= sync()
obj.sync1()
