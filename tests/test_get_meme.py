import pytest
import allure


@allure.feature('Get meme tests')
@allure.story('Get all memes test')
@pytest.mark.smoke
def test_get_full_meme_list(get_class, auth_token):
    get_class.get_full_meme_list(auth_token)
    get_class.check_data_is_exist(get_class.json)
    get_class.check_json_is_valid(get_class.json['data'])


@allure.feature('Get meme tests')
@allure.story('Get one meme')
@pytest.mark.smoke
def test_get_one(get_class, auth_token, base_class):
    get_class.get_one_meme(auth_token, base_class.generate_random_meme_id())
    get_class.check_one_meme(get_class.json)


@allure.feature('Get meme tests')
@allure.story('Get one meme with negative values')
@pytest.mark.regress
@pytest.mark.parametrize(
    'status_code, meme_id',
    [
        (200, 123),
        (404, 'keklol'),
        (404, 23452345),
        (404, '')
    ]
)
def test_validate_one(get_class, auth_token, status_code, meme_id):
    get_class.get_one_meme(auth_token, meme_id)
    get_class.check_status(status_code, get_class.status_code)


@allure.feature('Get meme tests')
@allure.story("Check that unauthorized user can't get meme")
@pytest.mark.smoke
def test_get_unauthorized(get_class, auth_token):
    get_class.get_full_meme_list(get_class.generate_random_token())
    get_class.check_status(401, get_class.status_code)
    get_class.get_one_meme(get_class.generate_random_token(), get_class.generate_random_meme_id)
    get_class.check_status(401, get_class.status_code)
