from app import settings
from utils.exceptions import APIException
from functools import wraps
from flask import request
from http.client import UNAUTHORIZED

def authorized_client(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_key = (request.headers.get('X-Auth-Key', '') or '').strip()
        if auth_key != settings.X_AUTH_KEY:
            raise APIException('Access restricted.', UNAUTHORIZED)

        return f(*args, **kwargs)
    return decorated_function