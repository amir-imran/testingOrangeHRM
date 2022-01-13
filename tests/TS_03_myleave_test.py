from selenium.webdriver.support.select import Select
import time

from selenium import webdriver
import pytest
import allure
import moment

from pages.loginPage import LoginPage
from pages.myleavePage import MyLeave
from utils import utils as environment

#to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")

class TestMyLeave():

    def test_login(self):
        driver = self.driver
        driver.get(environment.URL)

        login = LoginPage(driver)
        login.enter_username(environment.USERNAME)
        login.enter_password(environment.PASSWORD)
        login.click_login()

    def test_MyLeave(self):
        # declare
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        testName = environment.whoami()
        screenshotName = testName + "_screenshot_" + currTime
        driver =self.driver

        myleavePage = MyLeave(driver)
        myleavePage.click_myleave()
        myleavePage.click_date1()
        time.sleep(2)
        myleavePage.click_date2()
        time.sleep(2)
        # myleavePage.select_action()
        # time.sleep(3)
        myleavePage.first_scenario()
        time.sleep(5)
        myleavePage.second_scenario()
        # myleavePage.select_action1()
        # time.sleep(5)







