import random
import string
import pytest
import requests
from endpoints.base_enpdoint import BaseEndpoint
from endpoints.auth_endpoint import AuthEndpoint
from endpoints.post_meme_enpdoint import PostEndpoint
from endpoints.get_meme_endpoint import GetEndpoint
from endpoints.delete_meme_endpoint import DeleteEndpoint
from endpoints.put_meme_endpoint import PutEndpoint

url = 'http://167.172.172.115:52355/'
response = None
json = None
headers = None
auth_json = {'name': 'kek'}

@pytest.fixture()
def auth_class():
    return AuthEndpoint()

@pytest.fixture()
def base_class():
    return BaseEndpoint()


@pytest.fixture()
def post_class():
    return PostEndpoint()


@pytest.fixture()
def get_class():
    return GetEndpoint()

@pytest.fixture()
def put_class():
    return PutEndpoint()

@pytest.fixture()
def delete_class():
    return DeleteEndpoint()


@pytest.fixture()
def auth_token(base_class):
    old_token = base_class.read_file()
    response_check = requests.get(f'{url}authorize/{old_token}')
    if response_check.status_code == 404:
        response_new = requests.post(f'{url}authorize', json=auth_json).json()
        #headers = {'Authorization': response_new['token']}
        new_token = response_new['token']
        #print(new_token)
        base_class.write_file(new_token)
        return new_token
    elif response_check.text == 'Token is alive. Username is kek':
        #print(base_class.read_file)

        return old_token

