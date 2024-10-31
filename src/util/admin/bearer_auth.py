from requests.models import PreparedRequest
from requests.auth import AuthBase


class BearerAuth(AuthBase):
    def __init__(self, token: str) -> None:
        self.token = token

    def __call__(self, request: PreparedRequest):
        request.headers["Authorization"] = "Bearer " + self.token
        return request
