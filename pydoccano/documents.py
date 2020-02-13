from pathlib import Path

from requests import Session

from .base_api import BaseApi


class Documents(BaseApi):
    def __init__(self, base_url: str, session: Session, version='v1'):
        super().__init__(base_url)
        self.session = session
        self.version = version
        self.base_endpoint = f"{self.version}/projects"

    def list(self, project_id, offset=0, limit=100):
        return self._get(
            endpoint=f"{self.base_endpoint}/{project_id}/docs",
            params={
                'limit': limit,
                'offset': offset
            }
        )

    def details(self, project_id, doc_id):
        return self._get(endpoint=f"{self.base_endpoint}/{project_id}/docs/{doc_id}")

    def download(self, project_id, file_format='json'):
        return self._get(
            f"{self.base_endpoint}/{project_id}/docs/download?q={file_format}"
        )

    def upload(self, project_id, file_format, file_name, file_path):
        files = {
            'file': (
                file_name,
                open(Path(file_path, file_name), 'rb')
            )
        }
        data = {
            'file': (
                file_name,
                open(Path(file_path, file_name), 'rb')
            ),
            'format': file_format
        }
        return self._post(
            endpoint=f"{self.base_endpoint}/{project_id}/docs/upload",
            files=files,
            data=data
        )

