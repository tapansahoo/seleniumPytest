from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time
import json
import os
class FlightSelection(PageFactory):


    def __init__(self, driver):
        self.driver = driver
    #Declares a variable that will contain the retrieved text
    locators = {
            "Flight" : ('CSS', 'flights-summary > div > div:nth-child(1) > journey-container > journey > flight-list > div > flight-card > div > div > div.card-price.ng-tns-c159-10.ng-star-inserted > button'),
            "regular" : ('CSS', 'fare-table > div.fare-card-container > ry-spinner > div:nth-child(2) > fare-card > div'),
            "logintoRyanail" : ('CLASS_NAME', 'login-touchpoint__inner'),
            "passenger" : ('CLASS_NAME', "ngrx-forms-invalid ngrx-forms-pristine ngrx-forms-untouched ngrx-forms-unsubmitted"),
            "loginlater" : ('CLASS_NAME', "login-touchpoint__login-later"),
            "name" : ('XPATH', '// *[ @ id = "form.passengers.ADT-0.name"]'),
            "surname" : ('XPATH', '//*[@id="form.passengers.ADT-0.surname"]'),
            "title" : ("XPATH", '//*[@id="title-0-error-message"]/div[2]/button'),
            "Mr" : ( "CSS", "div.dropdown.b2.dropdown--opened > div > div > ry-dropdown-item:nth-child(1) > button"),
            "continuebutton" : ('CSS', "continue-flow-container > continue-flow > div > div > span > button"),
            "firstFlight":("XPATH","/html/body/flights-root/div/div/div/div/flights-lazy-content/flights-summary-container/flights-summary/div/div[1]/journey-container/journey/flight-list/div/flight-card"),
            "secondflight":("XPATH","/html/body/flights-root/div/div/div/div/flights-lazy-content/flights-summary-container/flights-summary/div/div[2]/journey-container/journey/flight-list/div/flight-card")

        }


    def selectflight(self):
        filepath = os.path.join(os.path.dirname(__file__), '..', 'testdata.json')
        print(filepath)
        f = open(filepath)
        data = json.load(f)
        self.firstFlight.click_button()
        self.secondflight.click_button()
        self.regular.click_button()
        self.loginlater.click_button()
        self.firstFlight.click_button()
        self.secondflight.click_button()


        title= '//*[@id="title-0-error-message"]/div[2]/button'
        name = '// *[ @ id = "form.passengers.ADT-0.name"]'
        surname = '//*[@id="form.passengers.ADT-0.surname"]'
        element = self.driver.find_elements(By.XPATH,title)
        for i in range(0,data['TestData']['Adult']):
            element[i].click()
            self.Mr.click_button()
            name = '//*[@id="form.passengers.ADT-' + str(i)+ '.name"]'
            surname='//*[@id="form.passengers.ADT-' +str(i)+ '.surname"]'
            self.driver.find_element(By.XPATH,name).send_keys(data['TestData']['Names'][i].split()[0])
            self.driver.find_element(By.XPATH,surname).send_keys(data['TestData']['Names'][i].split()[1])
        self.continuebutton.click_button()




