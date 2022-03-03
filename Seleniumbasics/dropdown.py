import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Seleniumbasics import logfile


class dpwon:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def dropdown(self):

        self.driver.get("http://www.leafground.com/pages/Dropdown.html")
       # self.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
        self.driver.implicitly_wait(50)
        daydropwn = Select(self.driver.find_element_by_id("dropdown1"))
        daydropwn.select_by_index(4)

        element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.NAME, "dropdown2")))

        monthdropwn = Select(self.driver.find_element_by_name("dropdown2"))
        monthdropwn.select_by_value("3")

        element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.NAME, "dropdown3")))

        yeardropwn = Select(self.driver.find_element_by_id("dropdown3"))
        yeardropwn.select_by_visible_text("Appium")

    def multiselectdropdown(self):
        #daydropwn = Select(self.driver.find_element_by_id("dropdown1"))
        #daydropwn.select_by_index(2)
        value = Select(self.driver.find_element_by_xpath("(//div[@class='example'])[6]//child::select"))
        multiselect= value.is_multiple
        print(multiselect)
        if multiselect == True :
            print("inside the if")
            value.select_by_index(1)
            value.select_by_index(2)
            value.select_by_value("3")
           # value.deselect_by_visible_text("Selenium")
            value.deselect_all()
dp=dpwon()
dp.dropdown()
dp.multiselectdropdown()

