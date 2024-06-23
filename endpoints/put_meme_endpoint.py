import allure
import requests
from endpoints.base_enpdoint import BaseEndpoint


class PutEndpoint(BaseEndpoint):
    @allure.step('Request to create meme')
    def put_meme(self, auth_token, payload, meme_id):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers={'Authorization': f'{auth_token}'}
        )
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.json = self.response.json()
            self.post_id = self.json['id']
        return self.response

    @allure.step('Check that get response is the same as put response')
    def check_get_response(self, get_response, post_response):
        self.are_equal(get_response, post_response, 'Get response is NOT the same as post response')
