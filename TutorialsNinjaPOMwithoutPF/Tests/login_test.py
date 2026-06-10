import pytest
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")

class TestLogin:
        def test_valid_login(self):

            homepage=HomePage(self.driver)
            homepage.click_login_button()
            loginpage=LoginPage(self.driver)
            loginpage.enter_login_details("demo.1@gmail.com","Demo123")
            actual_title = loginpage.login_title()
            assert actual_title=="My Account"
            


