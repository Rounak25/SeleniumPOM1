import unittest
from selenium import webdriver
from datetime import time
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..", ".."))
# sys.path.append(os.path.join(os.path.dirname(__file__),"..", ".."))
from POMDemo.Pages.LoginWindow import LoginPage
from POMDemo.Pages.HomePage import Homepage
import HtmlTestRunner

class Login_T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/cp/PycharmProjects/SeleniumPOM/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        a = LoginPage(driver)
        a.enter_username("Admin")
        time.sleep(2)
        a.enter_password("admin123")
        time.sleep(2)
        a.enter_login()

        b = Homepage(driver)
        b.click_on_welcome()
        b.click_on_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # #self.time.sleep(2)
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # #self.time.sleep(2)
        # self.driver.find_element_by_id("btnLogin").click()
        # #self.time.sleep(3)
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # #driver.find_elements_by_xpath("//*[@id="welcome-menu"]/ul/li[3]/a").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test Completed")

if __name__== "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/cp/PycharmProjects/SeleniumPOM/reports"))