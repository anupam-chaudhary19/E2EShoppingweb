from Locators import locators
from selenium import webdriver

class Signup():
    Button_Signup = "//*[@id='loginfrm']/div[4]/div[1]/a"
    textbox_firstname_name = "firstname"
    textbox_lastname_name = "lastname"
    textbox_mobilenum_name = "phone"
    textbox_emailid_name = "email"
    textbox_pwd_name = "password"
    textbox_c_pwd_name = "confirmpassword"
    Button_click_signup = "//*[@id='headersignupform']/div[8]/button"

    def __init__(self, driver):
        self.driver = driver

    def click_signup(self):
        self.driver.find_element_by_xpath(self.Button_Signup).click()

    def enter_firstname(self, firstname):
        self.driver.find_element_by_name(self.textbox_firstname_name).clear()
        self.driver.find_element_by_name(self.textbox_firstname_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_name(locators.Locators.textbox_lastname_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_lastname_name).send_keys(lastname)

    def enter_mobilenum(self, mobilenum):
        self.driver.find_element_by_name(locators.Locators.textbox_mobilenum_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_mobilenum_name).send_keys(mobilenum)

    def enter_emailid(self, emailid):
        self.driver.find_element_by_name(locators.Locators.textbox_emailid_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_emailid_name).send_keys(emailid)

    def enter_password(self, pwd):
        self.driver.find_element_by_name(locators.Locators.textbox_pwd_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_pwd_name).send_keys(pwd)

    def enter_confirmpwd(self, confirmpwd):
        self.driver.find_element_by_name(locators.Locators.textbox_c_pwd_name).clear()
        self.driver.find_element_by_name(locators.Locators.textbox_c_pwd_name).send_keys(confirmpwd)

    def clicksignup_submit(self):
        self.driver.find_element_by_xpath(self.Button_click_signup).click()
