import pytest
# from moduls.api.clients.github import GitHub

# @pytest.mark.api
# def test_user_exists():
#     api = GitHub()
#     user = api.get_user_defunkt()
#     assert user['login'] == "defunkt"

# @pytest.mark.api
# def test_user_non_exists():
#     api = GitHub()
#     r = api.get_not_exist_user()
#     print(r)
#     assert r['message'] == 'Not Found'

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('s_butenko')
    assert r['message'] == 'Not Found'
    
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 31
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_non_be_found(github_api):
    r = github_api.search_repo('become-qa-auto_aso')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_one_char_can_be_found(github_api):
    r = github_api.search_repo('b')
    assert r['total_count'] != 0
    


