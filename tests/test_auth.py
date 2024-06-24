import pytest
import allure


@allure.feature('Authorization tests')
@allure.story('Test typical аuthorization')
@pytest.mark.smoke
def test_normal_auth(auth_class):
    auth_class.auth()
    auth_class.check_status(200)
    auth_class.save_new_token()  # постусловие, чтобы не запрашивать часто токен
    # (не смог сделать нормальное постусловие через фикстуру, так как в нее нужно было бы передавать аргумент,
    # который будет известен только после завершения теста


@allure.feature('Authorization tests')
@allure.story('Check that token is alive')
@pytest.mark.regress
def test_is_token_alive(auth_class):
    auth_class.auth()
    auth_class.token_is_alive(auth_class.token)
    auth_class.check_status(200)
    auth_class.check_alive_message()
    auth_class.token_is_alive(auth_class.generate_random_token())
    auth_class.check_status(404)


@allure.feature('Authorization tests')
@allure.story('Check that token is correct')
@pytest.mark.regress
def test_token_is_correct(auth_class):
    auth_class.auth()
    auth_class.check_token()
