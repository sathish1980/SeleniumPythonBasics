import time

from selenium import webdriver

#driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe")
driver = webdriver.Edge("D:\Software\edgedriver_win64\msedgedriver.exe")
driver.maximize_window()
#driver.minimize_window()
#driver.set_window_size(200,700)
driver.get("https://en-gb.facebook.com/")
#driver.refresh()
#driver.get("https://www.gmail.com")
#driver.back()
#driver.forward()
#driver.quit()
#driver1 = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe");
#driver1.get("https://www.gmail.com")
#time.sleep(2)
username = driver.find_element_by_id("email")
username.send_keys("sahtishkumar")
username.clear()
username.send_keys("kumar.sathish189@gmail.com")
#username.send_keys("updatedvalue")
#paswword = driver.find_element_by_name("pass")
#paswword.send_keys("Admin@123")
#driver.find_element_by_name("login").click()

#driver.find_element_by_partial_link_text("ord?").click()
paswword = driver.find_element_by_css_selector("input[data-testid=royal_pass]")
paswword.send_keys("password123")
driver.find_element_by_xpath("//button[contains(@class,'selected') and @name='login']").click()
#driver.find_element_by_xpath("//button[contains(@class,'selected')]").click()
#driver.find_element_by_xpath("//button[contains(@id,'u_0_')]").click()
#driver.find_element_by_xpath("//button[starts-with(@id,'u_0_')]").click()
#driver.find_element_by_partial_link_text("password?").click()
#driver.find_element_by_class_name("inputtext _55r1 _6luy _9npi").send_keys("")"""
