import random
import string
import pytest
from endpoints.base_enpdoint import BaseEndpoint

@pytest.fixture()
def base_class():
    return BaseEndpoint()