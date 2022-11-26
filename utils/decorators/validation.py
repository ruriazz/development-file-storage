from app import settings
from flask import request
from werkzeug.datastructures import FileStorage
from utils.exceptions import APIException
from functools import wraps
from http.client import BAD_REQUEST

def validate_put_file(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == 'POST':
            file_object: FileStorage = request.files.get('object')
            storage_location = (request.form.get('location', '') or '').strip()

            if not file_object:
                raise APIException('unknown_object_file', BAD_REQUEST)

            if storage_location == '':
                raise APIException('unknown_storage_location', BAD_REQUEST)

            if file_object.mimetype not in settings.ALLOWED_MIMETYPE_UPLOAD:
                raise APIException('not_allowed_file')

        kwargs['request'] = request
        return f(*args, **kwargs)
    return decorated_function