import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Seleniumbasics.logfile import logdata


class lsthandle(logdata):

    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def listhand(self,actualtext):
        self.logfile()
        self.driver.get("https://www.makemytrip.com/")
        self.logger.warning("URL has been entered")
        time.sleep(4)
        self.driver.find_element_by_xpath("//li[@data-cy='account']").click()
        self.logger.warning("Element clicked")
        text_present=self.driver.find_element_by_class_name("langCardClose").is_displayed()
        self.logger.warning("bottom popup closed")
        if text_present == True:
            self.driver.find_element_by_class_name("langCardClose").click()
        self.driver.find_element_by_id("fromCity").click()
        self.logger.error("FromCity is clicked")
        time.sleep(2)
        totalvalue =self.driver.find_elements_by_xpath("/div[@class='react-autosuggest__section-container']//ul//li")
        sizeoflist = len(totalvalue) #20 will return
        print(sizeoflist)
        self.logger.critical("the size of the list is" +str(sizeoflist))
        for x in range(1,sizeoflist):

            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']//li["+str(x)+"]")))
            text_Value =  self.driver.find_element_by_xpath("//div[@id='react-autowhatever-1']//child::li["+str(x)+"]//div[2]").text
            print(text_Value)
            self.logger.critical("the value is :"+text_Value)
            if text_Value == actualtext:
                #time.sleep(4)
                self.driver.find_element_by_xpath("(//ul[@role='listbox']//li["+str(x)+"]//div)[1]").click()
                self.logger.critical("the given value is selected")
                break

    def Tolist(self,actualtext):
        #time.sleep(4)
        #self.driver.find_element_by_id("toCity").click()
        time.sleep(2)
        totalvalue =self.driver.find_elements_by_xpath("//ul[@role='listbox']//li")
        sizeoflist = len(totalvalue)
        print(sizeoflist)
        for x in range(1,sizeoflist):

            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']//li["+str(x)+"]")))
            text_Value =  self.driver.find_element_by_xpath("//ul[@role='listbox']//li["+str(x)+"]//div[2]").text
            print(text_Value)
            if text_Value == actualtext:
                #time.sleep(4)
                self.driver.find_element_by_xpath("(//ul[@role='listbox']//li["+str(x)+"]//div)[1]").click()
                break

l= lsthandle()
l.listhand("MAA")
#l.Tolist("BLR")