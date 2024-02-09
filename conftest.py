import random
import string
import pytest
from endpoints.base_enpdoint import BaseEndpoint
from endpoints.post_meme_enpdoint import PostEndpoint

@pytest.fixture()
def base_class():
    return BaseEndpoint()

@pytest.fixture()
def post_class():
    return PostEndpoint()
