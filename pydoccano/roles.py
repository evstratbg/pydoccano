from requests import Session

from .base_api import BaseApi


class Roles(BaseApi):
    def __init__(self, base_url: str, session: Session, version='v1'):
        super().__init__(base_url)
        self.session = session
        self.version = version
        self.base_endpoint = f"{self.version}/projects"

    def list(self, project_id):
        return self._get(
            f"{self.base_endpoint}/{project_id}/roles"
        )

    def details(self, project_id, rolemapping_id):
        return self._get(
            endpoint=f"{self.base_endpoint}/{project_id}/roles/{rolemapping_id}"
        )
