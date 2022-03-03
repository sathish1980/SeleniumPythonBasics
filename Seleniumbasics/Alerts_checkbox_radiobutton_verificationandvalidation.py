import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class dpwon:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def radiobutton(self):
        self.driver.get("http://www.leafground.com/pages/radio.html")
        self.driver.find_element_by_id("yes").click()
        self.driver.find_element_by_xpath("(//input[@name='news'])[2]").click()
    def checkbox(self):
        self.driver.get("http://www.leafground.com/pages/checkbox.html")
        displayedornot = self.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").is_displayed()
        if displayedornot == True:
            selectedornot=self.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").is_selected()
            if selectedornot==True:
                self.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        self.driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").click()
        self.driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").click()
    def Alert(self):
        self.driver.get("http://www.leafground.com/pages/Alert.html")
        self.driver.find_element_by_xpath("//button[text()='Alert Box']").click()
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='Confirm Box']").click()
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='Prompt Box']").click()
        obj = self.driver.switch_to.alert
        obj.send_keys("Besant technilogies")
        time.sleep(1)
        print(obj.text)
        obj.accept()
        self.driver.find_element_by_xpath("//button[text()='Sweet Alert']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='OK']").click()
    def verification(self):
        self.driver.get("http://www.leafground.com/pages/radio.html")
        #Get Title
        print(self.driver.title)
        # Get currenturl
        print(self.driver.current_url)
        # Get attribute
        classattributename = self.driver.find_element_by_id("yes").get_attribute("type")
        print(classattributename)
        # Get text
        classattribute = self.driver.find_element_by_xpath("//div[@id='first']//label[1]").text
        print(classattribute)

        # currentwindowname
        classattributename = self.driver.current_window_handle
        print(classattributename)
        classattributenames = self.driver.window_handles
        print(classattributenames)
    def validation(self):
        self.driver.get("http://www.leafground.com/pages/checkbox.html")
        time.sleep(2)
        print(self.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").is_displayed())
        valu= self.driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").is_selected()
        if valu == True :
            self.driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").click()
        print(self.driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").is_enabled())

d= dpwon()
d.verification()