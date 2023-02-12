import pytest

# it is not nessosory aftere conftest.py creation. This file uses fixture from common (specific) file - conftest.py
# class User:
#     def __init__(self):
#         self.name = "Olga"
#         self.second_name = "As"

# @pytest.fixture
# def user():
#     yield User()


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Olga'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'As'
