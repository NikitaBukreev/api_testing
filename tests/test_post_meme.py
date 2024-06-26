import pytest
import allure


BODY = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"ome": ["info1", "info2"], "two": ["info3", "info4"]}
}


@allure.feature('Post meme tests')
@allure.story('Create meme by post request with valid data')
@pytest.mark.smoke
def test_post_meme(post_class, get_class, auth_token, delete_class):
    post_class.post_meme(auth_token, BODY)
    meme_id = post_class.post_id
    post_class.check_json_is_valid()
    post_class.check_response_body_data(BODY)
    post_class.check_unique_body_data()
    get_class.get_one_meme(auth_token, meme_id)
    post_class.check_get_response(get_class.json)
    delete_class.delete_meme(auth_token, meme_id)


@allure.feature('Post meme tests')
@allure.story('Check that all fields are required')
@pytest.mark.regress
@pytest.mark.parametrize('deleted_key', ('text', 'url', 'tags', 'info'))
def test_post_meme_required_fields(post_class, auth_token, deleted_key):
    new_body = BODY.copy()
    del new_body[deleted_key]
    post_class.post_meme(auth_token, new_body)
    post_class.check_status(400)


@allure.feature('Post meme tests')
@allure.story('Check that all fields have validation on format')
@pytest.mark.regress
@pytest.mark.parametrize("key, value", [
    ('text', 123),              # подменяем строку числом
    ('text', []),               # подменяем строку списком
    ('url', 123),               # подменяем строку числом
    ('url', []),                # подменяем строку списком
    ('tags', "notalist"),       # подменяем список строкой
    ('tags', 123),              # подменяем список числом
    ('info', "notadict"),       # подменяем словарь строкой
    ('info', []),               # подменяем словарь списком
])
def test_post_meme_required_type_fields(post_class, auth_token, key, value):
    body = BODY.copy()
    body[key] = value
    post_class.post_meme(auth_token, body)
    post_class.check_status(400)


@allure.feature('Post meme tests')
@allure.story("Check that unauthorized user can't post meme")
@pytest.mark.smoke
def test_post_meme_unauthorized(post_class, auth_token):
    post_class.post_meme(post_class.generate_random_token(), BODY)
    post_class.check_status(401)
