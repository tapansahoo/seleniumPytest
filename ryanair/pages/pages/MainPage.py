from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import json
import time
import os
class MainPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
    """Home page action methods come here. I.e. Python.org"""
    #Declares a variable that will contain the retrieved text
    locators = {
        "destinationAirport": ('CSS', '#input-button__destination'),
        "departureAirport": ('CSS', '#input-button__departure'),
        "roundTrip" : ('CSS', ' fsw-flight-search-widget > fsw-trip-type-container > fsw-trip-type > fsw-trip-type-button:nth-child(1) > button'),
        "oneWay": ('CSS', 'sw-trip-type-container > fsw-trip-type > fsw-trip-type-button:nth-child(2)'),
        "cookie": ('CLASS_NAME', "cookie-popup-with-overlay__button"),
        "airport": ('CSS',
                    "fsw-airports-list > div.list__airports-container.ng-star-inserted > div.list__airports-scrollable-container.large-height > fsw-airport-item:nth-child(2)"),
        "choosDateSelector": ('CSS', 'fsw-input-button > div > div.input-button__input.ng-star-inserted'),

        "monthWidget": ('CSS', 'ry-datepicker-desktop > month-toggle > div > div.m-toggle__scrollable > div'),
        "dateselector": ('CSS', "[data-id='2022-03-25']"),
        "addAdult": (
        'CSS', "fsw-passengers-picker > ry-counter:nth-child(3) > div.counter > div:nth-child(3)"),
        "adultCount": (
        'CSS', 'fsw-passengers-picker > ry-counter:nth-child(3) > div.counter > div.counter__value'),
        "addChildren": (
        'CSS', "fsw-passengers-picker > ry-counter:nth-child(5) > div.counter > div:nth-child(3)"),
        "childernCount": (
        'CSS', "fsw-passengers-picker > ry-counter:nth-child(5) > div.counter > div.counter__value"),
        "done": ('CSS', "fsw-passengers-container > fsw-passengers > div > button"),
        "searchButton": ('CSS', ".flight-search-widget__start-search"),
        "passengerCount": ('CSS',
                           "fsw-input-button > div > div.input-button__input.input-button__display-value--truncate-text.ng-star-inserted")
    }



    def searchFlight(self):
        filepath = os.path.join(os.path.dirname(__file__), '..', 'testdata.json')
        print(filepath)
        f = open(filepath)
        data = json.load(f)
        self.cookie.click_button()
        self.roundTrip.click_button()
        self.departureAirport.click_button()
        self.departureAirport.clear_text()
        self.departureAirport.set_text(data['TestData']['place'][0])
        self.destinationAirport.click_button()
        self.destinationAirport.clear_text()
        self.destinationAirport.set_text(data['TestData']['place'][1])
        self.airport.click_button()
        self.choosDateSelector.click_button()
        self.choosDateSelector.click_button()
        element = self.driver.find_elements (By.CLASS_NAME, "m-toggle__month")
        # for ele in element:
        #      if ele.get_text() == str(data['TestData']['deptDate'][0]):
        #         ele.click()
        date_id_CSS ="[data-id="+ str("'"+data['TestData']['deptDate'][1]+"'") +"]"
        self.driver.find_element(By.CSS_SELECTOR,date_id_CSS).click()
        # element = self.driver.find_elements(By.CLASS_NAME, "m-toggle__month")
        # for ele in element:
        #      if ele.get_text() == str(data['TestData']['retDate'][0]):
        #         ele.click()
        date_id_CSS ="[data-id="+ str("'"+data['TestData']['retDate'][1]+"'") +"]"
        self.driver.find_element(By.CSS_SELECTOR,date_id_CSS).click()

        numofpassenger = int(self.passengerCount.get_text().split()[0])
        print (numofpassenger)

        for i in  range(0,int(data['TestData']['Adult'])-numofpassenger):
                    self.addAdult.click_button()

        # while self.driver.find_element(*MainPageLocators.childernCount).text != '1':
        #     self.driver.find_element(*MainPageLocators.addChildren).click()

        self.done.click_button()
        self.searchButton.click_button()
        time.sleep(3)

