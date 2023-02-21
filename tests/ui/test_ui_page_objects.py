import pytest
from moduls.ui.page_objects.sign_in_page import SignInPage


# test GitHub login-page accoding Page Object Model (transform test_ui.py)
@pytest.mark.ui
def test_check_incorrect_username():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login('sergeiibutenko@mistake.com', 'wrong_password')
    assert sign_in_page.check_title_name("Sign in to GitHub · GitHub")
    sign_in_page.close()