from http.client import BAD_REQUEST, METHOD_NOT_ALLOWED
from utils.api_response import ApiResponse
from app import app

class APIException(Exception):
    status: int = BAD_REQUEST

    def __init__(self, message=None, status: int=None, payload: dict=None):
        super().__init__()

        if status:
            self.status = status

        self.message = message
        self.payload = payload

@app.errorhandler(APIException)
def default_api_exception(e):
    return ApiResponse.error(
        data=e.payload if e.payload else e.message,
        status=e.status
    )

@app.errorhandler(METHOD_NOT_ALLOWED)
def method_not_allowed(e):
    from flask import request

    return ApiResponse.error(
        data=f'Method {request.method} not allowed.',
        status=METHOD_NOT_ALLOWED
    )