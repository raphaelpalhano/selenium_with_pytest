
import pytest
from  pageobject.pages.login_page import LoginPage

user1 = ['raphaelo1@gmail.com', 'abcd321', 'rafa'], ['testando123@gmail.com', 'teste123', 'testando']


@pytest.mark.parametrize('email, password, name', user1)
def test_login_user_valid(email, password, name, browser):
    login_page = LoginPage(browser)

    # Given acess barriga
    login_page.go_barriga()

    # When input email
    login_page.email(email)

    # and Input password
    login_page.password(password)

    # And click login
    login_page.click_sign()

    # Then display title:
    assert login_page.get_alert_text() in f'Bem vindo, {name}!'