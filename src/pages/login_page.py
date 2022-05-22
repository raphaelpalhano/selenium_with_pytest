"""
Module represent login page in barriga React: input email and password and click
in button for sign 
"""

from src.locators.login_locator import LoginLocator
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    URL = 'https://barrigareact.wcaquino.me/'

    def __init__(self, browser):
        self.browser = browser
    
    def go_barriga(self):
        self.browser.get(self.URL)
        

    def email(self, email):
        #WebDriverWait(self.browser, 1).until(self.browser.presence_of_element_located((By.ID, 'IdOfMyElement')))
        input_email = self.browser.find_element(*LoginLocator.INPUT_EMAIL())
        input_email.send_keys(email)
    
    def password(self, password):
        input_password = self.browser.find_element(*LoginLocator.INPUT_PASSWORD())
        input_password.send_keys(password)

    def click_sign(self):
        button_sign = self.browser.find_element(*LoginLocator.BUTTON_SIGN())
        button_sign.click()


    def get_alert_text(self):
        alert = self.browser.find_element(*LoginLocator.MESSAGE_LOGIN())
        return alert.text

