from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
class SeatSelection(PageFactory):

    def __init__(self, driver):
        self.driver = driver
    #Declares a variable that will contain the retrieved text
    locators = {
                   }

    def selectSeat(self):

        filepath = os.path.join(os.path.dirname(__file__), '..', 'testdata.json')
        print (filepath)
        f = open(filepath )
        data = json.load(f)
        print ("Hellow world")
        print(self.driver.current_url)
        time.sleep(5)

        seatelemnts =[ ele   for ele in  self.driver.find_elements(By.XPATH,"//*[contains(@id, 'seat-2')]") if ele.get_attribute("class")=='ng-star-inserted seatmap__seat seatmap__seat--standard']
       
        for i in range(0,2):
             # if ele.get_attribute("class")=='ng-star-inserted seatmap__seat seatmap__seat--standard':
            a = seatelemnts[i].get_attribute("id")
             #    b = ele.get_attribute("class")
             #    print(b)
             #    print(a)
            ele_xpath= '// *[ @ id = "'+ str(a)+'"]'
            print (ele_xpath)
            element = WebDriverWait(self.driver, 10).until(
                      EC.presence_of_element_located((By.XPATH,ele_xpath)))
            element.click()

        continueelemnt = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/seats-root/div/div/div/seats-container-root/seats-container-v2/main/div[2]/div/div/div/div/div/div[2]/div/seats-actions/span/button')))
        continueelemnt.click()

        seatContainer2nd = "/html/body/seats-root/div/div/div/seats-container-root/seats-container-v2/main/div[2]/div/div/div/div/div/div[1]/seat-map/div"
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, seatContainer2nd )))
        seatelemnts2 = [ele for ele in self.driver.find_elements(By.XPATH, "//*[contains(@id, 'seat-3')]") if
                        ele.get_attribute("class") == 'ng-star-inserted seatmap__seat seatmap__seat--standard']
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     for j in range(0, 2):
        #         a = seatelemnts2[i].get_attribute("id")
        #         #    b = ele.get_attribute("class")
        #         #    print(b)
        #         #    print(a)
        #         ele_xpath = '// *[ @ id = "' + str(a) + '"]'
        #         print(ele_xpath)
        #         element = WebDriverWait(self.driver, 20).until(
        #             EC.presence_of_element_located((By.XPATH, ele_xpath)))
        #         element.click()













