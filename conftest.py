import pytest
from moduls.api.clients.github import GitHub

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Olga"
        self.second_name = "As"

    # def create(self, name, second_name):
    #     self.name = name
    #     self.second_name = second_name

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    # before start testing
    user = User()
    user.create()

    yield user
    # after finish testing
    user.remove()

# 3. Modification of tests_github.py :
@pytest.fixture
def github_api():
    api = GitHub()
    yield api