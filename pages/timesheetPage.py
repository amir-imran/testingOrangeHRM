from selenium.webdriver.support.select import Select


class TimesheetPage:

    # 1. locator for Timesheet Page

    # naming convention : element_field_find element by what
    link_timesheet_xpath = "//*[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td[3]/div/a"
    input_employeeName_id = "employee"
    button_view_xpath = "//*[@id='btnView']"
    header_employeeNameTimesheet_xpath = "//*[@id='timesheet']/div/div[1]/h3"
    dropdown_date_id = "startDates"
    button_edit_id = "btnEdit"
    header_editEmployeeNameTimesheet_xpath = "//*[@id='edit-timesheet']/div/div[1]/h3"
    input_time_id = "initialRows_2_5"
    input_save_id = "submitSave"
    # link_logout_linktext = "Logout"

    # 2. python constructor

                        # the driver will be capture from test case and will be pass here
                        # to initiate the driver in this class
    def __init__(self,driver):
        self.driver=driver


    # 3. actions methods

                            # the username is the parameter that will be pass from the actual test case
                            # (test-login in testCases package)
    def clickTimesheet (self):
        self.driver.find_element_by_xpath(self.link_timesheet_xpath).click()

    def searchEmployeeName (self, employeeName):
        self.driver.find_element_by_id(self.input_employeeName_id).clear()
        self.driver.find_element_by_id(self.input_employeeName_id).send_keys(employeeName)

    def clickView (self):
        self.driver.find_element_by_xpath(self.button_view_xpath).click()

    def selectDate (self, dateSelected):
        date = self.driver.find_element_by_id(self.dropdown_date_id)
        selectDate = Select(date)

        selectDate.select_by_value(dateSelected)

    def checkCorrectEmployeeTimesheet (self) :
        flag = False
        employeeTimesheet = self.driver.find_element_by_xpath(self.header_employeeNameTimesheet_xpath).text

        print("Employee Timesheet : " + employeeTimesheet)

        # expected fail
        if employeeTimesheet == "Timesheet for Charlie Carter for Week1":
            flag = True

        return flag

    def checkCorrectEditEmployeeTimesheet (self) :
        flag = False
        editEmployeeTimesheet = self.driver.find_element_by_xpath(self.header_editEmployeeNameTimesheet_xpath).text

        print("Edit Employee Timesheet : " + editEmployeeTimesheet)

        # expected true
        if editEmployeeTimesheet == "Edit Timesheet for Charlie Carter for Week 2020-08-31":
            flag = True

        return flag

    def clickEdit (self) :
        self.driver.find_element_by_id(self.button_edit_id).click()

    def enterTimeData (self, time) :
        self.driver.find_element_by_id(self.input_time_id).clear()
        self.driver.find_element_by_id(self.input_time_id).send_keys(time)

    def clickSave (self):
        self.driver.find_element_by_id(self.input_save_id).click()


    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()