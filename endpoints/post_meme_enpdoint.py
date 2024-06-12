import allure
import requests

from endpoints.base_enpdoint import BaseEndpoint


class PostEndpoint(BaseEndpoint):

    post_id = None

    @allure.step('Request to create meme')
    def post_meme(self, auth_token, payload):
        self.response = requests.post(f'{self.url}/meme', json=payload, headers={'Authorization': f'{auth_token}'})
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response

    @allure.step('Check that body in response is the sam as in request')
    def check_response_body_data(self, body, response_json):
        common_keys = body.keys() & response_json.keys()
        self.are_equal(common_keys, {'info', 'text', 'url', 'tags'}, f"Where is no some keys in response")
        for key in common_keys:
            self.are_equal(
                body[key],
                response_json[key],
                f"Fields '{key}' in request and response are different: "
                f"in request '{body[key]}', but in response '{response_json[key]}'"
            )

    @allure.step('Check that unique keys are in response body')
    def check_unique_body_data(self, response_json):
        id_type = type(response_json['id'])
        updated_by = response_json['updated_by']
        auth_name = self.auth_json['name']
        self.are_equal(id_type, int, f'Needed int type if id, but given {id_type}')
        self.are_equal(updated_by, auth_name, f'Needed {auth_name} in updated_by, but given {updated_by}')

    @allure.step('Check that get response is the same as post response')
    def check_get_response(self, get_response, post_response):
        self.are_equal(get_response, post_response, 'Get response is NOT the same as post response')



