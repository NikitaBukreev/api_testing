import requests

from endpoints.base_enpdoint import BaseEndpoint


class PostEndpoint(BaseEndpoint):

    def post_meme(self):
        self.response = requests.post(self.url, json=self.json, headers=BaseEndpoint.auth())
        self.json = self.response.json()
        return self.response
