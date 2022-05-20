"""
Module represent login page in barriga React: input email and password and click
in button for sign 
"""

from src.locators.login_locator import LoginLocator
from selenium.webdriver.common.keys import Keys

class LoginPage:

    login_locator = LoginLocator()

    URL = 'https://barrigareact.wcaquino.me/'

    def __ini__(self, browser):
        self.browser = browser
    
    def go_barriga(self):
        self.browser.get(self.URL)

    def email(self, email):
        input_email = self.browser.find_element_by_css_selector(self.login_locator.get_email())
        input_email.send_keys(email)
    
    def password(self, password):
        input_password = self.browser.find_element_by_css_selector(self.login_locator.get_password())
        input_password.send_keys(password, Keys.ENTER)

    def click_sign(self):
        button_sign = self.browser.find_element_by_xpath(self.login_locator.get_button_sign())
        button_sign.click()



