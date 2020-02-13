from requests import Session

from .base_api import BaseApi


class Annotations(BaseApi):
    def __init__(self, base_url: str, session: Session, version='v1'):
        super().__init__(base_url)
        self.session = session
        self.version = version
        self.base_endpoint = f"{self.version}/projects"

    def list(self, project_id, doc_id):
        return self._get(
            endpoint=f"{self.base_endpoint}/{project_id}/docs/{doc_id}/annotations"
        )

    def details(self, project_id, doc_id, annotation_id):
        return self._get(
            endpoint=f"{self.base_endpoint}/{project_id}/docs/{doc_id}/annotations/{annotation_id}"
        )

    def statistics(self, project_id):
        return self._get(endpoint=f"{self.base_endpoint}/{project_id}/statistics")
