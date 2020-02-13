import requests
import json


class BaseApi:
    def __init__(self, base_url: str):
        self.session = requests.session()
        self.base_url = base_url.strip('/')

    def _get(self, endpoint: str, params: dict = None) -> json:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url=url, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: dict = None, files: dict = None, json: dict = None) -> json:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url=url, data=data, files=files, json=json)
        response.raise_for_status()
        return response.json()
