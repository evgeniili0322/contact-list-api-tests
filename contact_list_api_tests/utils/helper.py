import json
import os.path

import curlify
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response


def load_schema(name):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'json_schemas', name)
    with open(path) as file:
        json_schema = json.loads(file.read())
    return json_schema


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)
        curl = curlify.to_curl(response.request)

        with step(f'{method.upper()} {url} | Status Code: {response.status_code}'):
            allure.attach(body=curl.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            try:
                allure.attach(body=json.dumps(response.json(), indent=4).encode('utf8'), name='Response Json',
                              attachment_type=AttachmentType.JSON, extension='json')
            except:
                allure.attach(body=response.content, name='Response',
                              attachment_type=AttachmentType.TEXT, extension='txt')
            return response


users_api = CustomSession('https://thinking-tester-contact-list.herokuapp.com/users')
contacts_api = CustomSession('https://thinking-tester-contact-list.herokuapp.com')
