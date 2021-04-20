from concurrent.futures import thread

from selenium import webdriver
import unittest
import time
from Locators.Globalvariable import Globalvariable
from Pages import Loginpage
from Pages.Homepage import Homepage
from Pages.Loginpage import Loginpage
from Pages.Signup import Signup


class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= "C:/Users/Anupam/PycharmProjects/Travelwebautomation/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get(Globalvariable.baseURL)
        login = Loginpage(driver)
        login.enter_email(Globalvariable.username)
        login.enter_password(Globalvariable.password)
        login.clicklogin()
        time.sleep(5)
        page_title = self.driver.title
        if page_title == "My Account":
            assert True
        else:
            assert False

        login.clicklogout()

    def test_Signup(self):
        driver = self.driver
        driver.get(Globalvariable.baseURL)
        signup = Signup(driver)
        signup.click_signup()
        time.sleep(5)

        page_title1 = self.driver.title

        if page_title1 == "Register":
            assert True
        else:
            assert False

        signup.enter_firstname(Globalvariable.firstname)
        signup.enter_lastname(Globalvariable.lastname)
        signup.enter_mobilenum(Globalvariable.mobilenum)
        signup.enter_emailid(Globalvariable.emailid)
        signup.enter_password(Globalvariable.pwd)
        signup.enter_confirmpwd(Globalvariable.confirmpwd)
        signup.clicksignup_submit()

    def test_homepage(self):
        driver = self.driver
        driver.get(Globalvariable.baseURL)
        login = Loginpage(driver)
        login.enter_email(Globalvariable.username)
        login.enter_password(Globalvariable.password)
        login.clicklogin()
        time.sleep(5)
        homepage = Homepage(driver)
        homepage.click_home()
        time.sleep(5)
        page_title1 = self.driver.title
        if page_title1 == "PHPTRAVELS | Travel Technology Partner":
            assert True
        else:
            assert False

        homepage.click_hotels()
        time.sleep(5)
        page_title2 = self.driver.title
        if page_title2 == "PHPTRAVELS | Travel Technology Partner":
            assert True
        else:
            assert False
        time.sleep(5)

        homepage.click_tours()
        page_title3 = self.driver.title
        if page_title3 == "PHPTRAVELS | Travel Technology Partner":
            assert True
        else:
            assert False
        time.sleep(5)

        homepage.click_flights()
        page_title3 = self.driver.title
        if page_title3 == "PHPTRAVELS | Travel Technology Partner":
            assert True
        else:
            assert False
        time.sleep(5)

        homepage.click_tour_thailand()
        page_title4 = self.driver.title

        if page_title4 == "6 Days Around Thailand":
            assert True
        else:
            assert False

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()




