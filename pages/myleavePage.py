from selenium.webdriver.support.select import Select


class MyLeave:

    def __init__(self, driver):
        self.driver = driver

        #self.sellect_MyLeave_xpath = "(//span[normalize-space()='My Leave'])[1]"
        self.sellect_MyLeave_xpath = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/a[1]/span[1]"
        self.sellect_Date1_xpath = "(//img[@class='ui-datepicker-trigger'])[1]"
        self.sellect_startTime_xpath = "(//a[normalize-space()='9'])[1]"
        self.sellect_Date2_xpath = "(//img[@class='ui-datepicker-trigger'])[2]"
        self.sellect_EndTime2_xpath = "//a[normalize-space()='31']"
        self.sellect_untickAll_xpath = "(//input[@id='leaveList_chkSearchFilter_checkboxgroup_allcheck'])[1]"
        self.click_search_btn_id = "btnSearch"
        self.sellect_tick_cancel_xpath = "(//input[@id='leaveList_chkSearchFilter_0'])[1]"
        self.untick_cancel_xpath = "(//input[@id='leaveList_chkSearchFilter_0'])[1]"
        self.tick_scheduled_id = "leaveList_chkSearchFilter_2"
        self.click_saveButton_id = "btnSave"



    def click_myleave(self):
        self.driver.find_element_by_xpath(self.sellect_MyLeave_xpath).click()

    def click_date1(self):
        self.driver.find_element_by_xpath(self.sellect_Date1_xpath).click()
        self.driver.find_element_by_xpath(self.sellect_startTime_xpath).click()

    def click_date2(self):
        self.driver.find_element_by_xpath("(//img[@class='ui-datepicker-trigger'])[2]").click()
        selectMonth = self.driver.find_element_by_xpath("(//select[@class='ui-datepicker-month'])[1]")
        dropdown = Select(selectMonth)
        self.driver.implicitly_wait(5)
        dropdown.select_by_visible_text("Jul")
        self.driver.implicitly_wait(5)
        selectdate2 = self.driver.find_element_by_xpath("(//a[normalize-space()='31'])[1]").click()
        self.driver.find_element_by_id(self.click_search_btn_id).click()

    def select_action(self):
        selectAction = self.driver.find_element_by_xpath("(//select[@id='select_leave_action_69'])[1]")
        dropdownAction = Select(selectAction)
        self.driver.implicitly_wait(5)
        dropdownAction.select_by_visible_text("Cancel")
        self.driver.implicitly_wait(5)
        #select_save = driver.find_element_by_name("btnSave").click()
        #self.driver.find_element_by_name(self.select_save_name).click

    def first_scenario(self):
        self.driver.find_element_by_xpath(self.sellect_untickAll_xpath).click()
        self.driver.find_element_by_xpath(self.sellect_tick_cancel_xpath).click()
        self.driver.find_element_by_id(self.click_search_btn_id).click()

    def second_scenario(self):
        self.driver.find_element_by_xpath(self.untick_cancel_xpath).click()
        self.driver.find_element_by_id(self.tick_scheduled_id).click()
        self.driver.find_element_by_id(self.click_search_btn_id).click()

    def select_action1(self):
        selectAction1 = self.driver.find_element_by_name("select_leave_action_69")
        dropdownAction1 = Select(selectAction1)
        self.driver.implicitly_wait(5)
        dropdownAction1.select_by_visible_text("Select Action")
        self.driver.implicitly_wait(5)
        # select_save = self.driver.find_element_by_id("btnSave").click()
        self.driver.find_element_by_id(self.click_saveButton_id).click()
        self.driver.implicitly_wait(5)


        # selectAction1 = self.driver.find_element_by_name("select_leave_action_69")
        # dropdownAction1 = Select(selectAction1)
        # #self.driver.implicitly_wait(5)
        # dropdownAction1.select_by_visible_text("Cancel")
        # #self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id(self.select_save_id).click