from selenium import webdriver
import unittest
from Locators import locators
from Locators.Globalvariable import Globalvariable


class Loginpage():

    textbox_email_name = locators.Locators.textbox_email_name
    textbox_password = locators.Locators.textbox_password_name
    click_logout = locators.Locators.Button_logout_xpath


    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, username):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(locators.Locators.textbox_password_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(locators.Locators.button_Login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(locators.Locators.Button_logout_xpath).click()
        self.driver.find_element_by_xpath(locators.Locators.Click_Logout_xpath).click()

