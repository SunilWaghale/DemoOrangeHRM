import time

import pytest

from pageObjects.LoginPage import Login
from utilities.Logger import LogGen
from utilities.Readconfigfile import ReadValue


class Test_Url_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    Url = ReadValue.getUrl()
    log = LogGen.loggen()

    @pytest.mark.Sanity
    def test_Url_001(self, setup):
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Going to Url")
        time.sleep(2)
        self.log.info("Checking page title")
        if self.driver.title == "OrangeHRM":
            self.log.info("test_Url_001 is Passed ")
            self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_Url_001_pass.png")
            assert True
        else:
            self.log.info("test_Url_001 is Failed ")
            self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_Url_001_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_Url_001 is Completed ")

    @pytest.mark.Sanity
    def test_login_002(self,setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Going to Url")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter UserName-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on login button")
        if self.lp.login_status() == True:
            self.log.info("test_login_002 is Passed")
            self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_002_pass.png")
            self.lp.Click_Menu_Button()
            self.log.info("Click on menu button")
            self.lp.Click_logout_Button()
            self.log.info("Click on logout button")
            assert True
        else:
            self.log.info("test_login_002 is Failed")
            self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_002_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_login_002 is Completed")