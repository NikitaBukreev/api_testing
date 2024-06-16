import allure
import string
import random
import requests


class BaseEndpoint:

    url = 'http://167.172.172.115:52355/'
    response = None
    json = None
    auth_json = {'name': 'kek'}
    auth_json_another_user = {'name': 'another_kek'}
    status_code = None
    token = None
    user = None
    response_text = None

    @allure.step('Check elements are equal')
    def are_equal(self, a, b, message):
        assert a == b, message

    @allure.step('Read token.txt file')
    def read_file(self):
        try:
            with open('token.txt', 'r') as token_file:
                token = token_file.readline()
                return token
        except FileNotFoundError:
            with open('token.txt', 'a+'):
                pass
            return None

    @allure.step('Write token.txt file')
    def write_file(self, new_token):
        with open('token.txt', 'w') as token_file:
            token_file.write(new_token)

    @allure.step('Generate random token')
    def generate_random_token(self):
        my_string = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(my_string, k=15))
        return random_string

    @allure.step('Generate random meme id')
    def generate_random_meme_id(self):
        return random.randint(1, 5000)

    @allure.step('Check response status')
    def check_status(self, expected_status, real_status):
        self.are_equal(expected_status, real_status, f'Need {expected_status} but given {real_status}')

    @allure.step('Check that response json have valid format')
    def check_json_is_valid(self, response_json):
        def validate_json(item):
            expected_keys = {
                'id': int,
                'info': dict,
                'tags': list,
                'text': str,
                'updated_by': str,
                'url': str
            }

            for key, expected_type in expected_keys.items():
                if key not in item:
                    return False, f"Missing key '{key}' in item"
                if not isinstance(item[key], expected_type):
                    return False, f"Type mismatch for key '{key}': expected {expected_type}, got {type(item[key])}"
            return True, None

        # Проверяем, является ли response_json списком или словарем
        if isinstance(response_json, list):
            for idx, entry in enumerate(response_json):
                is_valid, error_message = validate_json(entry)
                if not is_valid:
                    self.are_equal(is_valid, True,
                                   f'Found not valid element in json response at index {idx}: {error_message}')
        elif isinstance(response_json, dict):
            is_valid, error_message = validate_json(response_json)
            self.are_equal(is_valid, True, f'Found not valid element in json response: {error_message}')
        else:
            self.are_equal(False, True, f'Unexpected response_json type: {type(response_json)}')

    @allure.step('Check that unique keys are in response body')
    def check_unique_body_data(self, response_json):
        id_type = type(response_json['id'])
        updated_by = response_json['updated_by']
        auth_name = self.auth_json['name']
        self.are_equal(id_type, int, f'Needed int type in id, but given {id_type}')
        self.are_equal(updated_by, auth_name, f'Needed {auth_name} in updated_by, but given {updated_by}')

    @allure.step('Auth by another user')
    def auth_another_user(self):
        self.response = requests.post(f'{self.url}authorize', json=self.auth_json_another_user)
        self.json = self.response.json()
        self.token = self.json['token']
        self.user = self.json['user']
        return self.response

    @allure.step('Check author name')
    def check_author_name(self, expected_name, result_name):
        self.are_equal(
            expected_name,
            result_name,
            f'Needed author {expected_name}, but given another author {result_name}'
        )
