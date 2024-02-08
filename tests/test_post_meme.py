import pytest
import requests

url = 'http://167.172.172.115:52355/'
response = None
json = None
auth_json = {'name': 'kek'}
BODY = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"ome": ["info1", "info2"], "two": ["info3", "info4"]}
}

def test_post():
    auth_token = requests.post('http://167.172.172.115:52355/authorize', json={'name': 'kek'}).json()
    post_meme = requests.post('http://167.172.172.115:52355/meme', json=BODY, headers={'Authorization': auth_token['token']})
    print(post_meme.json())
