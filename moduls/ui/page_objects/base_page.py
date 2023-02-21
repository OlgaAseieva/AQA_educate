from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# test GitHub login-page accoding Page Object Model (transform test_ui.py)
class BasePage():

    PATH = r'/d:/AQA_GL/AQA_educate/chromdriver_win32/'
    DRIVER_NAME = r'cromedriver.exe'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
        service = Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )
    def close(self):
        self.driver.close()