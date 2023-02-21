import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_correct_username():
    # object creation
    driver = webdriver.Chrome(
        service=Service(r'/d:/AQA_GL/AQA_educate/chromdriver_win32/' + r'cromedriver.exe')
    )
    # opaning of page
    driver.get('https://github.com/login')

    # searching of page element (field of form)
    login_elem = driver.find_element(By.ID, "login_field")
    # send incorrect email
    login_elem.send_keys('sergeiibutenko@mistake.com')
    # time.sleep(3)

    password_elem = driver.find_element(By.ID, "password")
    password_elem.send_keys('wrong_password')
    # time.sleep(3)

    # finding of buttom "Sign in" and buttom click emitation
    btm_elem = driver.find_element(By.NAME, 'commit')
    btm_elem.click 
    # time.sleep(2)

    # check of page-title name
    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()