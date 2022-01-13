import time

from selenium import webdriver
import pytest
import allure
import moment

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.timesheetPage import TimesheetPage
from utils import utils as environment

#to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")

class TestTimesheet ():


    def test_login(self):

        driver = self.driver
        driver.get(environment.URL)

        # login
        login = LoginPage(driver)
        login.enter_username(environment.USERNAME)
        login.enter_password(environment.PASSWORD)
        login.click_login()
        time.sleep(2)


    def test_timesheetView(self):

        # declare
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        testName = environment.whoami()
        screenshotName = testName + "_screenshot_" + currTime

        driver = self.driver


        # go to timesheet
        timesheet = TimesheetPage(driver)
        timesheet.clickTimesheet()


        # view employee timesheet
        timesheet.searchEmployeeName("Charlie Carter")
        timesheet.clickView()

        empTmSheet = timesheet.checkCorrectEmployeeTimesheet()

        try:

            assert True == empTmSheet

        except AssertionError as viewError:

            print("Assertion error occurred")
            print(viewError)


            # save screenshot in allure
            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "D://n//UTM//intern//tm rnd//automation test//orangeHrmAutomationTest//screenshots//" +
                screenshotName + ".png")

        time.sleep(3)


        # view employee timesheet for selected date
        timesheet.selectDate("5")

        time.sleep(3)


        # edit employee timesheet
        timesheet.clickEdit()

        editEmpTmSheet = timesheet.checkCorrectEditEmployeeTimesheet()

        try:

            assert True == editEmpTmSheet

        except :

            print("error edit employee timesheet")


            # save screenshot in allure
            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "D://n//UTM//intern//tm rnd//automation test//orangeHrmAutomationTest//screenshots//" +
                screenshotName + ".png")

        time.sleep(3)


        # editing employee timesheet
        timesheet.enterTimeData("3:00")

        time.sleep(3)

        timesheet.clickSave()

        time.sleep(3)


    def test_logout (self):

        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        testName = environment.whoami()
        screenshotName = testName + "_screenshot_" + currTime

        # logout
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)

            # save screenshot in allure
            allure.attach(driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            #to get the file on specific path
            driver.get_screenshot_as_file("D://n//UTM//intern//tm rnd//automation test//orangeHrmAutomationTest//screenshots//"+
                                   screenshotName+".png")
            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = environment.whoami()
            screenshotName = testName + "_screenshot_" + currTime
            # save screenshot in allure
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            # to get the file on specific path
            driver.get_screenshot_as_file(
                "D://n//UTM//intern//tm rnd//automation test//orangeHrmAutomationTest//screenshots//" +
                screenshotName + ".png")
            #the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("Inside finally block")

        time.sleep(3)
