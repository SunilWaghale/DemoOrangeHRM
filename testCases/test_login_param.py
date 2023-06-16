import time

import pytest

from pageObjects.LoginPage import Login
from utilities.Logger import LogGen
from utilities.Readconfigfile import ReadValue


class Test_Login_Params:
    Url = ReadValue.getUrl()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_params_003(self,setup,getDataForLogin):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Going to Url")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(getDataForLogin[0])
        self.log.info("Enter UserName-->" + getDataForLogin[0])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Enter Password-->" + getDataForLogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")
        login_stauts=[]
        if self.lp.login_status() == True:
            if getDataForLogin[2] == "Pass":
                login_stauts.append("Pass")
                self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_params_003_pass.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on menu button")
                self.lp.Click_logout_Button()
                self.log.info("Click on logout button")
            elif getDataForLogin[2] == "Fail":
                login_stauts.append("Fail")
                self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_params_003_pass.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on menu button")
                self.lp.Click_logout_Button()
                self.log.info("Click on logout button")

            #assert True
        else:
            if getDataForLogin[2] == "Fail":
                login_stauts.append("Pass")
                self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_params_003_fail.png")
            elif getDataForLogin[2] == "Pass":
                login_stauts.append("Fail")
                self.driver.save_screenshot("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Screenshots\\test_login_params_003_fail.png")
        print(login_stauts)

        if "Fail" not in login_stauts:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_params_003 is Completed")