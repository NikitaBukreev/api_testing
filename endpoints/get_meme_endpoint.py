import requests
import allure
from endpoints.base_enpdoint import BaseEndpoint


class GetEndpoint(BaseEndpoint):

    @allure.step('Request to get all full meme list')
    def get_full_meme_list(self, auth_token):
        self.response = requests.get(f'{self.url}/meme', headers={'Authorization': f'{auth_token}'})
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.json = self.response.json()
        return self.response

    @allure.step('Request to get only one meme')
    def get_one_meme(self, auth_token, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers={'Authorization': f'{auth_token}'})
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.status_code = self.response.status_code
            self.json = self.response.json()
        return self.response

    @allure.step("Check that 'data' is in list")
    def check_data_is_exist(self):
        self.are_equal(list(self.json.keys())[0], 'data', 'There is no data in response json')

    @allure.step('Check that response json have only one meme')
    def check_one_meme(self):
        id_count = 0
        for item in self.json:
            if 'id' in item:
                id_count += 1

        self.are_equal(1, id_count, f'Need only 1 meme, but given {id_count}')
