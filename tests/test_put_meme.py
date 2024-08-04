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
def test_put_meme(put_class, post_class, get_class, auth_token, delete_class):
    # создаем и проверяем, что мем создался
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    body_put["id"] = meme_id
    posted_meme = get_class.get_one_meme(auth_token, meme_id)
    post_class.check_get_response(posted_meme.json())

    # изменяем и проверяем, что изменения применились
    put_class.put_meme(auth_token, body_put, meme_id)
    put_class.check_json_is_valid()
    edited_meme = get_class.get_one_meme(auth_token, meme_id)
    put_class.check_get_response(edited_meme.json())

    # проверяем, что уникальные поля на месте
    get_class.check_unique_body_data()
    delete_class.delete_meme(auth_token, meme_id)


@allure.feature('Edit meme tests')
@allure.story('Check that all fields are required')
@pytest.mark.regress
@pytest.mark.parametrize('deleted_key', ('text', 'url', 'tags', 'info', 'id'))
def test_put_meme_required_fields(put_class, post_class, auth_token, deleted_key, delete_class):
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    body_put['id'] = meme_id
    del body_put[deleted_key]
    put_class.put_meme(auth_token, body_put, meme_id)
    put_class.check_status(400)
    delete_class.delete_meme(auth_token, meme_id)


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
def test_put_meme_required_type_fields(put_class, post_class, auth_token, key, value, delete_class):
    body_put = BODY_PUT.copy()
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    body_put['id'] = meme_id
    body_put[key] = value
    put_class.put_meme(auth_token, body_put, post_class.post_id)
    put_class.check_status(400)
    delete_class.delete_meme(auth_token, meme_id)


@allure.feature('Edit meme tests')
@allure.story("Check that only the meme's author can edit it")
@pytest.mark.smoke
def test_edit_meme_another_user(put_class, auth_token, base_class, post_class, get_class, delete_class):
    # Тут два варианта:
    # 1) можно сделать дополнительную авторизацию для генерации нового токена на другое имя
    # 2) а можно просто гетать рандомный мем и проверять, кто его автор, если автор не я, то пытаться изменить
    # первый способ более правильный (так как если получится внести изменения, то нехорошо менять чужие мемы),
    # второй более простой. Выбрал первый способ
    base_class.auth_another_user()
    another_token = base_class.token
    post_class.post_meme(another_token, BODY_POST)
    meme_id = post_class.post_id
    get_class.get_one_meme(auth_token, meme_id)
    base_class.check_author_name(get_class.json['updated_by'])
    BODY_PUT['id'] = meme_id
    put_class.put_meme(auth_token, BODY_PUT, meme_id)
    put_class.check_status(403)
    delete_class.delete_meme(another_token, meme_id)


@allure.feature('Edit meme tests')
@allure.story("Check that id in request path and request body must be the same")
@pytest.mark.regress
def test_edit_meme_different_id(put_class, auth_token, post_class, delete_class):
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    random_meme_id = post_class.generate_random_meme_id()

    BODY_PUT['id'] = meme_id
    put_class.put_meme(auth_token, BODY_PUT, random_meme_id)
    put_class.check_status(403)

    BODY_PUT['id'] = random_meme_id
    put_class.put_meme(auth_token, BODY_PUT, meme_id)
    put_class.check_status(400)

    delete_class.delete_meme(auth_token, meme_id)


@allure.feature('Edit meme tests')
@allure.story("Check that unauthorized user can't edit meme")
@pytest.mark.smoke
def test_put_meme_unauthorized(post_class, put_class, auth_token):
    post_class.post_meme(auth_token, BODY_POST)
    meme_id = post_class.post_id
    BODY_PUT['id'] = meme_id
    put_class.put_meme(put_class.generate_random_token(), BODY_PUT, meme_id)
    put_class.check_status(401)
