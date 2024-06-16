import allure
import pytest


BODY = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"ome": ["info1", "info2"], "two": ["info3", "info4"]}
}


@allure.feature('Delete meme tests')
@allure.story('Delete new created meme')
@pytest.mark.smoke
def test_delete_meme(delete_class, post_class, get_class, auth_token):
    post_class.post_meme(auth_token, BODY)
    meme_id = post_class.post_id
    get_class.get_one_meme(auth_token, meme_id)
    get_class.check_status(200, get_class.status_code)
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(200, delete_class.status_code)
    delete_class.check_delete_message(delete_class.response_text, meme_id)
    get_class.get_one_meme(auth_token, meme_id)
    get_class.check_status(404, get_class.status_code)


@allure.feature('Delete meme tests')
@allure.story("Check that only the meme's author can delete it")
@pytest.mark.regress
def test_delete_meme_another_user(delete_class, post_class, get_class, base_class, auth_token):
    base_class.auth_another_user()
    post_class.post_meme(base_class.token, BODY)
    meme_id = post_class.post_id
    get_class.get_one_meme(auth_token, meme_id)
    base_class.check_author_name(base_class.auth_json_another_user['name'], get_class.json['updated_by'])
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(403, delete_class.status_code)
    delete_class.delete_meme(base_class.token, meme_id)
    delete_class.check_status(200, delete_class.status_code)
    delete_class.check_delete_message(delete_class.response_text, meme_id)


@allure.feature('Delete meme tests')
@allure.story('Check delete endpoint with different ids')
@pytest.mark.regress
@pytest.mark.parametrize('meme_id', [321321, 'kek', '$%^&', ''])
def test_delete_meme_with_diff_id(delete_class, post_class, get_class, auth_token, meme_id):
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(404, delete_class.status_code)


@allure.feature('Delete meme tests')
@allure.story('Try to delete one meme two times')
@pytest.mark.regress
def test_two_times_delete(delete_class, post_class, get_class, auth_token):
    post_class.post_meme(auth_token, BODY)
    meme_id = post_class.post_id
    get_class.get_one_meme(auth_token, meme_id)
    get_class.check_status(200, get_class.status_code)
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(200, delete_class.status_code)
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(404, delete_class.status_code)


@allure.feature('Delete meme tests')
@allure.story("Check that unauthorized user can't delete meme")
@pytest.mark.smoke
def test_delete_meme_unauthorized(delete_class, post_class, get_class, auth_token):
    post_class.post_meme(auth_token, BODY)
    meme_id = post_class.post_id
    get_class.get_one_meme(auth_token, meme_id)
    get_class.check_status(200, get_class.status_code)
    delete_class.delete_meme(delete_class.generate_random_token(), meme_id)
    delete_class.check_status(401, delete_class.status_code)
    delete_class.delete_meme(auth_token, meme_id)
    delete_class.check_status(200, delete_class.status_code)
