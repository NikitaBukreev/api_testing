import pytest
import allure


BODY_POST = {
    "text": "kek",
    "url": "lol.ru",
    "tags": ["yes", "no"],
    "info": {"one": ["info1", "info2"], "two": ["info3", "info4"]}
}

BODY_PUT = {
    "text": "put_kek",
    "url": "put_lol.ru",
    "tags": ["put_yes", "put_no"],
    "info": {"put_one": ["put_info1", "put_info2"], "put_two": ["put_info3", "put_info4"]}
}


@allure.feature('Edit meme tests')
@allure.story('Edit new created meme')
@pytest.mark.smoke
def test_put_meme(put_class, post_class, get_class, auth_token):
    # создаем и проверяем, что мем создался
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    body_put["id"] = meme_id
    posted_meme = get_class.get_one_meme(auth_token, meme_id)
    post_class.check_get_response(posted_meme.json(), post_class.json)

    # изменяем и проверяем, что изменения применились
    put_class.put_meme(auth_token, body_put, meme_id)
    put_class.check_json_is_valid(put_class.json)
    edited_meme = get_class.get_one_meme(auth_token, meme_id)
    put_class.check_get_response(edited_meme.json(), put_class.json)

    #проверяем, что уникальные поля на месте
    put_class.check_unique_body_data(edited_meme.json())
    # TODO Не забыть удалить мем когда будет готов метод удаления


@allure.feature('Edit meme tests')
@allure.story('Check that all fields are required')
@pytest.mark.regress
@pytest.mark.parametrize('deleted_key', ('text', 'url', 'tags', 'info', 'id'))
def test_put_meme_required_fields(put_class, post_class, auth_token, deleted_key):
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    body_put['id'] = post_class.post_id
    del body_put[deleted_key]
    put_class.put_meme(auth_token, body_put, post_class.post_id)
    put_class.check_status(400, put_class.status_code)
    # TODO Не забыть удалить мем когда будет готов метод удаления


@allure.feature('Edit meme tests')
@allure.story('Check that all fields have validation on format')
@pytest.mark.regress
@pytest.mark.parametrize("key, value", [
    ('id', 'notint'),
    ('id', []),
    ('text', 123),
    ('text', []),
    ('url', 123),
    ('url', []),
    ('tags', "notalist"),
    ('tags', 123),
    ('info', "notadict"),
    ('info', []),
])
def test_put_meme_required_type_fields(put_class, post_class, auth_token, key, value):
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    body_put['id'] = post_class.post_id
    body_put[key] = value
    put_class.put_meme(auth_token, body_put, post_class.post_id)
    post_class.check_status(400, put_class.status_code)
    # TODO Не забыть удалить мем когда будет готов метод удаления


@allure.feature('Edit meme tests')
@allure.story('Edit new created meme')
@pytest.mark.smoke
def test_normal_auth(put_class, auth_token):

    # изменение чужого мема, проверка поля updated be
    # тут два варианта:
    # 1) можно сделать дополнительную авторизацию для генерации нового токена на другое имя
    # 2) а можно просто гетать рандомный мем и проверять, кто его автор, если автор не я, то пытаться изменить
    # первый способ более правильный, второй более простой
    pass

@allure.feature('Edit meme tests')
@allure.story('Edit new created meme')
@pytest.mark.smoke
def test_normal_auth(put_class, auth_token):
    # изменение отличающимеся айди в урле и теле
    pass

@allure.feature('Edit meme tests')
@allure.story('Edit new created meme')
@pytest.mark.smoke
def test_normal_auth(put_class, auth_token):
    # изменение с невалидными параметрами
    pass

@allure.feature('Edit meme tests')
@allure.story('Edit new created meme')
@pytest.mark.smoke
def test_normal_auth(put_class, auth_token):
    # изменение без авторизации
    pass