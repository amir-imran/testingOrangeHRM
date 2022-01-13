from selenium.webdriver.common.by import By

class LeaveListPage():

    def __init__(self, driver):
        self.driver = driver

        self.leave_list_xpath = '//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[2]/div/a'
        self.from_date_id = 'calFromDate'
        self.to_date_id = 'calToDate'
        self.pending_approval_id = 'leaveList_chkSearchFilter_1'
        self.search_button_id = 'btnSearch'

    def click_leaveList(self):
        self.driver.find_element(By.XPATH, self.leave_list_xpath).click()

    def input_dateFrom(self):
        self.driver.find_element(By.ID, self.from_date_id).clear()
        self.driver.find_element(By.ID, self.from_date_id).send_keys("2021-04-20")

    def input_dateTo(self):
        self.driver.find_element(By.ID, self.to_date_id).clear()
        self.driver.find_element(By.ID, self.to_date_id).send_keys("2022-01-22")

    def untick_box(self):
        self.driver.find_element(By.ID, self.pending_approval_id).click()

    def click_searchBtn(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

