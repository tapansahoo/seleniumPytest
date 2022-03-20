from selenium import webdriver
from pages.MainPage import MainPage
from pages.FlightSelection import FlightSelection
from pages.SeatSelection import SeatSelection
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

import pytest
import time

class TestCases():
    """A sample test class to show how page object works"""

    @pytest.fixture
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='/root/ryanair/chromedriver')


        # caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        # self.driver = webdriver.Remote( 'http://138.68.151.187:4444/wd/hub',
        #       DesiredCapabilities.CHROME)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get("https://www.ryanair.com")

    def test_testCase1(self,setUp):
        print ("hello1")
        main_page= MainPage(self.driver)
        main_page.searchFlight()
        print("hello2")
        time.sleep(5)
        flight_selection=FlightSelection(self.driver)
        print("hello3")
        flight_selection.selectflight()
        time.sleep(5)
        print("hello4")
        seat_selection=SeatSelection(self.driver)
        seat_selection.selectSeat()
    #     time.sleep(5)
    #     flight_selection = Flightselection(self.driver)
    #     flight_selection.selectflight()
    #     time.sleep(5)
    #     Seat_selection = SeatSelection(self.driver)
    #     Seat_selection.selectSeat()
    def tearDown(self):
        self.driver.close()

