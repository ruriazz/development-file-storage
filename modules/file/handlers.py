from app import app
from urllib import parse
from flask import request
from utils.exceptions import APIException
from http.client import BAD_REQUEST
from .services import FileService

@app.route('/file', methods=['GET'])
def read_file_storage():
    object_location = parse.unquote((request.args.get('obj', '') or '').strip())

    if object_location == '':
        raise APIException('unknown_object', BAD_REQUEST)

    return FileService.read_file(object_location)