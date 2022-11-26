import json
from app import app
from http.client import IM_USED, OK, BAD_REQUEST

class ApiResponse:
    @staticmethod
    def __response(status: int, error: int = None, data=None, headers: dict = {}):
        response = {"success": False, "http_code": status}

        if data:
            response["content"] = data

        if status >= OK and status <= IM_USED:
            response["success"] = True
        else:
            if 'content' in response:
                del response["content"]

            response["errors"] = data
            response["error_code"] = error


        if data and isinstance(data, str):
            if "content" in response:
                del response["content"]
            else:
                del response["errors"]

            response["message"] = data

        status = status

        return app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )

    @staticmethod
    def success(data=None, status: int = OK, headers: dict = {}):
        return ApiResponse.__response(data=data, status=status, headers=headers)

    @staticmethod
    def error(data=None, code: int = None, status: int = BAD_REQUEST, headers: dict = {}):
        return ApiResponse.__response(status, code, data, headers)
