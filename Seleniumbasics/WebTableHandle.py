
from selenium import webdriver
from selenium.webdriver.support.select import Select


class webtab:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def table(self,actualtext):
        self.driver.get("http://www.leafground.com/pages/table.html")
        totalrowvalue = self.driver.find_elements_by_xpath("//table[@id='table_id']//tr")
        sizeofrowlist = len(totalrowvalue)
        for x in range(2, sizeofrowlist+1):
            totalcolumnvalue = self.driver.find_elements_by_xpath("//table[@id='table_id']//tr[" + str(x) + "]//td")
            sizeofcolumnlist = len(totalcolumnvalue)
            text_Value = self.driver.find_element_by_xpath("//table[@id='table_id']//tr[" + str(x) + "]//td[1]").text
            print(text_Value)
            if text_Value != actualtext:
                self.driver.find_element_by_xpath("//table[@id='table_id']//tr[" + str(x) + "]//td[3]//input").click()
                #break
W= webtab()
W.table("Learn XPath")