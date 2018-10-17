import requests
import certifi
import urllib3
import json
import utils
import pyodbc
import os
from config import base_url
from commons import authentication
from commons import endpoints
from pages.page import Page
import datetime


class AuthenticatePage(Page):
    def __init__(self):
        super(AuthenticatePage, self)
        self.BASE_URL = os.getenv('BASE_URL', base_url.CADEV_API)
        self.auth_header = self._get_auth_header()

    def _get_auth_header(self):
        payload = authentication.PAYLOAD

        r = requests.get(url=endpoints.AUTHENTICATE_ENDPOINT.format(self.BASE_URL),
                         data=payload,
                         verify=True)

        r_content = json.loads(r.content)
        auth_header = {authentication.AUTHORIZATION_HEADER:
                           authentication.AUTHORIZATION_BEARER.format(r_content[authentication.ACCESS_TOKEN])}
        print(json.dumps(r_content))

        return auth_header
