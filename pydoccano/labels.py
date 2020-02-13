from requests import Session

from .base_api import BaseApi


class Labels(BaseApi):
    def __init__(self, base_url: str, session: Session, version='v1'):
        super().__init__(base_url)
        self.session = session
        self.version = version
        self.base_endpoint = f"{self.version}/projects"

    def list(self, project_id):
        return self._get(endpoint=f"{self.base_endpoint}/{project_id}/labels")

    def details(self, project_id, label_id):
        return self._get(endpoint=f"{self.base_endpoint}/{project_id}/labels/{label_id}")

    def post_approve_labels(self, project_id, doc_id):
        return self._post(
            f"{self.base_endpoint}/{project_id}/docs/{doc_id}/approve-labels"
        )

