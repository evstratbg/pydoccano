from requests import Session

from .base_api import BaseApi


class Features(BaseApi):
    def __init__(self, base_url: str, session: Session, version='v1'):
        super().__init__(base_url)
        self.session = session
        self.version = version
        self.base_endpoint = f"{self.version}/features"

    def get(self):
        return self._get(endpoint=self.base_endpoint)
