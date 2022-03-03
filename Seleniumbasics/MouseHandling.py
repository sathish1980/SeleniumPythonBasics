import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys


class Mousehandle:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def mouse(self):
        self.driver.get("http://www.leafground.com/pages/mouseOver.html")
        self.driver.maximize_window()
        elec = self.driver.find_element_by_xpath("//a[text()='TestLeaf Courses']")
        ac = ActionChains(self.driver)
        ac.move_to_element(elec).click_and_hold().release().move_to_element(self.driver.find_element_by_xpath("//a[text()='RPA']")).click().perform()

    def draganddrop(self):
        self.driver.get("http://www.leafground.com/pages/drop.html")
        self.driver.maximize_window()
        elec = self.driver.find_element_by_id("draggable")
        ac = ActionChains(self.driver)
        ac.move_to_element(elec).drag_and_drop(elec,self.driver.find_element_by_id("droppable")).perform()

    def facebook(self):
        self.driver.get("https://en-gb.facebook.com/")
        usrnamr = self.driver.find_element_by_id("email")
        ac = ActionChains(self.driver)
        ac.move_to_element(usrnamr).send_keys("sathish").double_click().context_click().perform()
        pyautogui.press(['down', 'down', 'down'])
        pyautogui.press('enter')
        # time.sleep(10)
        # ac.key_down('tab')
        # ac.key_up('tab')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'v')
    """ time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)"""



    def ebaysite(self):
        self.driver.get("https://www.ebay.com/")
        electornics=self.driver.find_element_by_xpath("(//a[text()='Electronics'])[2]")
        ac = ActionChains(self.driver)
        ac.move_to_element(electornics).perform()
        ac.move_to_element(self.driver.find_element_by_xpath("//a[text()='Computers and tablets']")).click().perform()


a= Mousehandle()
a.facebook()