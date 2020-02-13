from requests.models import Response

from .base_api import BaseApi
from .users import Users
from .projects import Projects
from .features import Features
from .roles import Roles
from .labels import Labels
from .documents import Documents
from .annotations import Annotations


class Doccano(BaseApi):
    def __init__(self, base_url: str, username: str, password: str, version='v1'):
        super().__init__(base_url)
        self.version = version
        self.__login(username, password)
        self.users = Users(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.projects = Projects(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.features = Features(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.roles = Roles(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.labels = Labels(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.documents = Documents(
            base_url=base_url,
            session=self.session,
            version=version
        )
        self.annotations = Annotations(
            base_url=base_url,
            session=self.session,
            version=version
        )

    def get_me(self):
        return self._get(endpoint=f"{self.version}/me")

    def __login(self, username: str, password: str) -> Response:
        auth = {
            'username': username,
            'password': password
        }
        response_json = self._post(endpoint='v1/auth-token', data=auth)
        token = response_json['token']
        self.session.headers.update(
            {
                'Authorization': f"Token {token}",
                'Accept': 'application/json'
            }
        )
