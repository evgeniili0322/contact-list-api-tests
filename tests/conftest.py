import os

import pytest
from dotenv import load_dotenv

from contact_list_api_tests.utils.helper import users_api


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
    pytest.user_data = {'email': os.getenv('EMAIL'), 'password': os.getenv('PASSWORD')}


@pytest.fixture(scope='function')
def delete_registered_user():
    response = users_api.post(
        '/login',
        json={
            'email': pytest.user_data['email'],
            'password': pytest.user_data['password']
        }
    )

    if response.status_code == 200:
        users_api.delete(
            '/me',
            headers={'Authorization': response.json()['token']}
        )


@pytest.fixture(scope='session')
def auth_token():
    response = users_api.post(
        '/login',
        json={
            'email': pytest.user_data['email'],
            'password': pytest.user_data['password']
        }
    )

    return response.json()['token']
