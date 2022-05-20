"""
Cobertura de teste do login no barriga react.
"""



from src.pages.login_page import LoginPage


def test_login_user_valid(browser):
    login_page = LoginPage(browser)

    # Given acess barriga
    login_page.go_barriga()

    # When input email
    login_page.email('testando123@gmail.com')

    # and Input password
    login_page.password('teste123')

    # And click login
    login_page.click_sign()

    # Then display title:
