import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(f'Response is: {r.text}')

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/s_butenko')
    assert r.status_code == 404
    print(f'Response Stasus code is: {r.status_code}')

@pytest.mark.http
def test_third_request():
    r = requests.get('https://api.github.com/users/OlgaAseieva')
    body = r.json()
    headers = r.headers
    # defunkt - forbidern 
    # print(f'Response is: {r.text}')
    # print(f'Response Body: {r.json()}')
    print(f'Response Stasus code is: {r.status_code}')
    assert body['login'] == 'OlgaAseieva'
    assert r.status_code == 200
    # print(f'Response Headers are: {r.headers}')
    assert headers ['Server']== 'GitHub.com' 