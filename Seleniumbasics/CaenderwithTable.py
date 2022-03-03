from selenium import webdriver
from selenium.webdriver.support.select import Select


class calwithtable:
    driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
    def table(self,actualvalue):
        self.driver.get("http://www.leafground.com/pages/Calendar.html")
        self.driver.find_element_by_id("datepicker").click()
        totalrowvalue = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr")
        sizeofrowlist = len(totalrowvalue)
        print(sizeofrowlist)
        for x in range(1, sizeofrowlist+1):
            totalcolumnvalue = self.driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr["+str(x) +"]//td")
            sizeofcolumnlist = len(totalcolumnvalue)
            print(sizeofcolumnlist)
            for y in range(1, sizeofcolumnlist+1):
                text_Value = self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr["+str(x) +"]//td["+str(y) +"]").get_attribute("class")

                if text_Value.__contains__('disabled'):
                    print("novalue")
                else:
                    calendervalue=self.driver.find_element_by_xpath(
                        "//table[@class='ui-datepicker-calendar']//tbody//tr[" + str(x) + "]//td[" + str(
                            y) + "]//a").text
                    print(calendervalue)
                    if calendervalue == actualvalue:
                        self.driver.find_element_by_xpath(
                            "//table[@class='ui-datepicker-calendar']//tbody//tr[" + str(x) + "]//td[" + str(
                                y) + "]").click()
                        break

                    #break
tab= calwithtable()
tab.table("1")