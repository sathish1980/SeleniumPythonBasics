import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.select import Select


class uplod:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def upl(self):
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("(//div[@class='input-file-upload-hover-placeholder']//parent::div)[1]").click()
        pyperclip.copy("D:\\Besant\\JAVA\\Java basics.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print("uploaded sucessfully")

e =uplod()
e.upl()