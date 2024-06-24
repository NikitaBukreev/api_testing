import requests
import allure
from endpoints.base_enpdoint import BaseEndpoint


class AuthEndpoint(BaseEndpoint):
    token = None
    user = None

    @allure.step('Take auth token')
    def auth(self):
        self.response = requests.post(f'{self.url}authorize', json=self.auth_json)
        self.json = self.response.json()
        self.token = self.json['token']
        self.user = self.json['user']
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Check that token is alive')
    def token_is_alive(self, token):
        self.response = requests.get(f'{self.url}authorize/{token}')
        self.status_code = self.response.status_code
        self.response_text = self.response.text
        return self.response

    @allure.step('Check response status')
    def check_status(self, expected_status):
        self.are_equal(expected_status, self.status_code, f'Need {expected_status} but given {self.status_code}')

    @allure.step('Check message in response')
    def check_alive_message(self):
        self.are_equal(
            f"Token is alive. Username is {self.auth_json['name']}",
            self.response_text,
            f"Need 'Token is alive....' but given \'{self.response_text}\'"
        )

    @allure.step('Save new token for use in other tests')
    def save_new_token(self):
        self.read_file()
        self.write_file(self.token)

    @allure.step('Check the count of symbols in token')
    def check_token(self):
        self.are_equal(15, len(self.token), f'Need 15 symbols in token, but given {len(self.token)}')
