from moduls.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# test GitHub login-page accoding Page Object Model (transform test_ui.py)
class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)

        password_elem = self.driver.find_element(By.ID, "password")
        password_elem.send_keys(password)

        btm_elem = self.driver.find_element(By.NAME, 'commit')
        btm_elem.click

    def check_title_name(self, expected_title):
        return self.driver.title == expected_title 