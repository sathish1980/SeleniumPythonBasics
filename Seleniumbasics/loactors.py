import time

from selenium import webdriver


class locator:
    print("started")
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
   # driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
   #driver = webdriver.Edge('D:\Software\edgedriver_win64_93\msedgedriver.exe')
    def launch(self):
        self.driver.get("https://en-gb.facebook.com/")
        time.sleep(1)
        self.driver.maximize_window()
       # self.driver.minimize_window();
      #  self.driver.set_window_size(300,600)
       # self.driver.maximize_window()
       # self.driver.close()

        username=self.driver.find_element_by_id("email")
        username.send_keys("sathishkumar")
        username.clear();
        time.sleep(60)
        username.send_keys("sathishkumar_Updated")
        password = self.driver.find_element_by_name("pass")
        password.send_keys("sathishkumar")
        #login = self.driver.find_element_by_ta("login")
        #login.click()
        linktext=self.driver.find_element_by_link_text("Forgotten password?")
        linktext.click()
        linktext = self.driver.find_element_by_partial_link_text("Forgotten")
        linktext.click()

        #self.driver.quit()
obj=locator()
obj.launch()