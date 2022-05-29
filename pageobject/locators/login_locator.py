from selenium.webdriver.common.by import By



class LoginLocator:
    

    def INPUT_EMAIL(): return By.CSS_SELECTOR, 'input[data-test="email"]'
    def INPUT_PASSWORD(): return By.CSS_SELECTOR, 'input[data-test="passwd"]'
    def BUTTON_SIGN(): return By.XPATH, '//button[text()="Entrar"]'
    def MESSAGE_LOGIN(): return By.XPATH, '//div[@class="toast-message"]'
    