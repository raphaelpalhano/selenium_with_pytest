from selenium.webdriver.common.by import By

class LoginLocator:

    def __init__(self):
        self.__INPUT_EMAIL = (By.CSS_SELECTOR, 'input[data-test="email"]')
        self.__INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[data-test="passwd"]')
        self.__BUTTON_SIGN = (By.XPATH, '//button[text()="Entrar"]')

    def get_email(self):
        return  self.__INPUT_EMAIL
    
    def get_password(self):
        return self.__INPUT_PASSWORD 
    
    def get_button_sign(self):
        return self.__BUTTON_SIGN