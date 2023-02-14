
import pytest

#  2. moved to conftest.py
# class User:
#     def __init__(self) -> None:
#         self.name = None
#         self.second_name = None

#     def create(self):
#         self.name = "Olga"
#         self.second_name = "As"

#     def remove(self):
#         self.name = ""
#         self.second_name = ""

#  1. modified to fixture stucture 
# def test_change_name():
#         user = User()
#         user.create()

#         assert user.name == "Olga"
#         user.remove()

#  1. modified to fixture stucture
# def test_change_second_name():
#         user = User()
#         user.create()

#         assert user.second_name == "As"
#         user.remove()

#  2. moved to conftest.py
# @pytest.fixture
# def user():
#     user = User()
#     user.create()

#     yield user
#     user.remove()


@pytest.mark.check
def test_change_name(user):
    assert user.name == "Olga"

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == "As"



# @pytest.mark.parametrize(
#         "name, second_name",
#           [('Olga', 'As'),
#            ('Sergii', 'Butenko')])
# def user(name, second_name):
#     assert user.name == name
#     assert user.second_name == second_name


    
