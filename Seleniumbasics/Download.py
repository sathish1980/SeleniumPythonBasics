import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.support.select import Select


class download:
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\SeleniumProject\\Downloadfile\\"}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe', options=options)

    def downdefaultlocation(self):
        driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
        driver.get("http://www.leafground.com/pages/download.html")
        driver.maximize_window()
        driver.find_element_by_link_text("Download Excel").click()
        time.sleep(5)

    def downspecificlocation(self):
        self.driver.get("http://www.leafground.com/pages/download.html")
        #self.driver.maximize_window()
        self.driver.find_element_by_link_text("Download Excel").click()




D = download()
D.downspecificlocation()
