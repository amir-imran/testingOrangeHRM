from selenium.webdriver.common.by import By

class AssignLeave:

    def __init__(self, driver):
        self.driver = driver

        self.assign_leave_link_xpath = '/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[1]'
        self.leave_name_id = "assignleave_txtEmployee_empName"
        self.leave_type_box_id = "assignleave_txtLeaveType"
        self.leave_type_xpath = "//*[@id='assignleave_txtLeaveType']/option[2]"
        self.leave_from_box_id = "assignleave_txtFromDate"
        self.leave_from_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]/a'
        self.leave_to_box_id = "assignleave_txtToDate"
        self.leave_to_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]/a'
        self.submit_id = "assignBtn"

        # self.welcome_link_id = "welcome"
        # self.logout_link_linkText = "Logout"

    def click_assignleave(self):
        self.driver.find_element(By.XPATH, self.assign_leave_link_xpath).click()

    def enter_leavename(self):
        self.driver.find_element(By.ID, self.leave_name_id).send_keys("Odis Adalwin")

    def input_leavetype(self):
        self.driver.find_element(By.ID, self.leave_type_box_id).click()
        self.driver.find_element(By.XPATH, self.leave_type_xpath).click()

    def input_leavefrom(self):
        self.driver.find_element(By.ID, self.leave_from_box_id).click()
        self.driver.find_element(By.XPATH, self.leave_from_xpath).click()

    def input_leaveto(self):
        self.driver.find_element(By.ID, self.leave_to_box_id).click()
        self.driver.find_element(By.XPATH, self.leave_to_xpath).click()

    def input_submit(self):
        self.driver.find_element(By.ID, self.submit_id).click()