import requests

from endpoints.base_enpdoint import BaseEndpoint


class PostEndpoint(BaseEndpoint):

    def post_meme(self, payload):
        BaseEndpoint.auth(self)
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=self.headers)
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response
