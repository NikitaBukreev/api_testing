import requests
import pytest
import random


class BaseEndpoint:

    url = 'http://167.172.172.115:52355/'
    response = None
    json = None
    auth_json = {'name': 'kek'}

    def auth(self):
        self.response = requests.post(f'{self.url}authorize', json=self.auth_json).json()
        return self.response['token']
