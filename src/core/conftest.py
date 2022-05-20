import pytest
from selenium import webdriver



@pytest.fixture
def setup():

    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

    