import pytest
import allure
import requests


BODY = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"ome": ["info1", "info2"], "two": ["info3", "info4"]}
}


@allure.feature('Post meme tests')
@allure.story('Create meme by post request with valid data')
@pytest.mark.smoke
def test_post_meme(post_class, get_class, auth_token):
    post_class.post_meme(auth_token, BODY)
    post_class.check_json_is_valid(post_class.json)
    post_class.check_response_body_data(BODY, post_class.json)
    post_class.check_unique_body_data(post_class.json)
    get_class.get_one_meme(auth_token, post_class.post_id)
    post_class.check_get_response(get_class.json, post_class.json)
    # TODO Не забыть удалить мем когда будет готов метод удаления


@allure.feature('Post meme tests')
@allure.story('Check that all fields are required')
@pytest.mark.regress
def test_post_meme_required_fields(post_class, auth_token):
    pass

def test_post_meme_required_type_fields(post_class, auth_token):
    pass

def test_post_meme_unauthorized(post_class, auth_token):
    pass

