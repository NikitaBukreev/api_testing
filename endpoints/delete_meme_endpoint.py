import requests
import allure

from endpoints.base_enpdoint import BaseEndpoint


class DeleteEndpoint(BaseEndpoint):

    @allure.step('Check that token is alive')
    def delete_meme(self, auth_token, meme_id):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{auth_token}'}
        )
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.response_text = self.response.text
        return self.response

    @allure.step('Check message in response')
    def check_delete_message(self, real_message, meme_id):
        self.are_equal(
            f"Meme with id {meme_id} successfully deleted",
            real_message,
            f"Need 'Meme with id....deleted' but given \'{real_message}\'"
        )
