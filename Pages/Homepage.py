from selenium import webdriver
from Locators import locators

class Homepage():
    Link_home_xpath = locators.Locators.Link_homepage
    Link_hotels_xpath = locators.Locators.Link_hotels
    Link_tours_xpath = locators.Locators.Link_Tours
    Link_flights_xpath = locators.Locators.Link_flights
    Link_tour_thailand_xpath = locators.Locators.Link_TourThailand

    def __init__(self, driver):
        self.driver = driver

    def click_home(self):
        self.driver.find_element_by_xpath(self.Link_home_xpath).click()

    def click_hotels(self):
        self.driver.find_element_by_xpath(self.Link_hotels_xpath).click()

    def click_tours(self):
        self.driver.find_element_by_xpath(self.Link_tours_xpath).click()

    def click_flights(self):
        self.driver.find_element_by_xpath(self.Link_flights_xpath).click()

    def click_tour_thailand(self):
        self.driver.find_element_by_xpath(self.Link_tour_thailand_xpath).click()
