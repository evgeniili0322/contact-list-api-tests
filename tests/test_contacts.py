import allure
import jsonschema
from allure import step
from allure_commons.types import Severity

from contact_list_api_tests.utils.helper import contacts_api, load_schema
from contact_list_api_tests.data.contact_data import contact_data


@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('contacts')
@allure.title('Add contact schema validation')
def test_add_contact_schema_validation(auth_token):
    schema = load_schema('add_contact.json')

    response = contacts_api.post(
        '/contacts',
        json={
            'firstName': contact_data.first_name,
            'lastName': contact_data.last_name,
            'birthdate': contact_data.birthdate,
            'email': contact_data.email,
            'phone': contact_data.phone
        },
        headers={'Authorization': auth_token}
    )

    with step('Assert response status code'):
        assert response.status_code == 201
    with step('Assert json schema'):
        jsonschema.validate(response.json(), schema)


@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('contacts')
@allure.title('Add contact response body')
def test_add_contact_response_body(auth_token):
    response = contacts_api.post(
        '/contacts',
        json={
            'firstName': contact_data.first_name,
            'lastName': contact_data.last_name,
            'birthdate': contact_data.birthdate,
            'email': contact_data.email,
            'phone': contact_data.phone
        },
        headers={'Authorization': auth_token}
    )

    with step('Assert response body'):
        assert response.json()['firstName'] == contact_data.first_name
        assert response.json()['lastName'] == contact_data.last_name
        assert response.json()['birthdate'] == contact_data.birthdate
        assert response.json()['email'] == contact_data.email
        assert response.json()['phone'] == contact_data.phone


@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('contacts')
@allure.title('Get contact list schema validation')
def test_get_contact_list_schema_validation(auth_token):
    schema = load_schema('get_contact_list.json')

    response = contacts_api.get('/contacts', headers={'Authorization': auth_token})

    with step('Assert response status code'):
        assert response.status_code == 200
    with step('Assert json schema'):
        jsonschema.validate(response.json(), schema)


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('contacts')
@allure.title('Delete contact')
def test_delete_contact(auth_token):
    contact_list = contacts_api.get('/contacts', headers={'Authorization': auth_token})
    contact_id = contact_list.json()[0]['_id']

    response = contacts_api.delete(f'/contacts/{contact_id}', headers={'Authorization': auth_token})

    with step('Assert response status code'):
        assert response.status_code == 200
    with step('Assert deleted contact'):
        assert response.text == 'Contact deleted'
