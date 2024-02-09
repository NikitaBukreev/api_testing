import pytest
import requests
from conftest import base_class, post_class

url = 'http://167.172.172.115:52355'
response = None
json = None
auth_json = {'name': 'kek'}
BODY = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"ome": ["info1", "info2"], "two": ["info3", "info4"]}
}

def test_post_positive(base_class, post_class):
    # auth_token = requests.post('http://167.172.172.115:52355/authorize', json={'name': 'kek'}).json()
    # post_meme = requests.post('http://167.172.172.115:52355/meme', json=BODY, headers={'Authorization': auth_token['token']}).json()

    post_class.post_meme(BODY)


    # get_meme = requests.get(f"http://167.172.172.115:52355/meme/{post_meme['id']}", headers={'Authorization': auth_token['token']}).json()
    # assert post_meme == get_meme
    # assert get_meme['updated_by'] == 'kek'
    # del get_meme['id']
    # del get_meme['updated_by']
    # assert BODY == get_meme
    # del_meme = requests.delete(f"http://167.172.172.115:52355/meme/{post_meme['id']}", headers={'Authorization': auth_token['token']}).text
    # assert del_meme == f"Meme with id {post_meme['id']} successfully deleted"
    # get_meme2 = requests.get(f"http://167.172.172.115:52355/meme/{post_meme['id']}", headers={'Authorization': auth_token['token']}).status_code
    # assert get_meme2 == 404

