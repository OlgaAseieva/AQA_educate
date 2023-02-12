import pytest

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Olga"
        self.second_name = "As"

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