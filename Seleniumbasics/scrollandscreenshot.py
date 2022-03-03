import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys


class scrllscrn:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def scroll(self):
        self.driver.get("http://www.leafground.com/home.html")
        self.driver.maximize_window()
        #scroll down
        self.driver.execute_script("window.scrollTo(0, 500)","")
        s.screenshot("testcase1")
        time.sleep(1)
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -600)", 0)
        time.sleep(1)
        s.screenshot("testcase2")
        # scroll right
        self.driver.execute_script("window.scrollTo(600, 0)", 0)
        time.sleep(1)
        s.screenshot("testcase3")
        # scroll left
        self.driver.execute_script("window.scrollTo(-600, 0)", 0)

        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        s.screenshot("testcase4")
        self.driver.execute_script("window.scrollTo(0, 0)","")
        # screenshot
        s.screenshot("testcase5")

        # scroll to a specific element
        element=self.driver.find_element_by_xpath("//h5[text()='Window']//parent::a")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        s.screenshot("testcase6")
        #screenshot
       # root_path=os.path.dirname("\\screenshot\\image.png")
        #root_path = os.path.dirname(os.path.abspath("image.png"))
        #ROOT_DIR = os.path.abspath(os.curdir)

        #print(root_path)
        #print(ROOT_DIR)


    def screenshot(self,filename):
        self.driver.save_screenshot(
            "C:\\Users\\sathishkumar\\PycharmProjects\\SeleniumProject\\screenshot\\"+filename+".png")

s = scrllscrn()
s.scroll()