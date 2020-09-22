from POMDemo.Locators.locators1 import Locators
class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_button_id = Locators.click_on_welcome
        self.logout_button_link_text = Locators.click_on_logout

    def click_on_welcome(self):
        self.driver.find_element_by_id(Locators.click_on_welcome).click()

    def click_on_logout(self):
        self.driver.find_element_by_link_text(Locators.click_on_logout).click()