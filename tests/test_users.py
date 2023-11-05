import jsonschema
import pytest
from allure import step

from contact_list_api_tests.utils.helper import users_api, load_schema


def test_add_user_schema_validation(delete_registered_user):
    schema = load_schema('post_users.json')

    response = users_api.post(
        '',
        json={
            'firstName': 'Test',
            'lastName': 'User',
            'email': pytest.user_data['email'],
            'password': pytest.user_data['password']
        }
    )

    with step('Assert response status code'):
        assert response.status_code == 201
    with step('Assert json schema'):
        jsonschema.validate(response.json(), schema)


def test_login_schema_validation():
    schema = load_schema('post_users.json')

    response = users_api.post(
        '/login',
        json={
            'email': pytest.user_data['email'],
            'password': pytest.user_data['password']
        }
    )

    with step('Assert response status code'):
        assert response.status_code == 200
    with step('Assert json schema'):
        jsonschema.validate(response.json(), schema)


def test_login_response_body():
    response = users_api.post(
        '/login',
        json={
            'email': pytest.user_data['email'],
            'password': pytest.user_data['password']
        }
    )

    with step('Assert response body'):
        assert response.json()['user']['firstName'] == 'Test'
        assert response.json()['user']['lastName'] == 'User'
        assert response.json()['user']['email'] == pytest.user_data['email']
