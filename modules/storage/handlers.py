from app import app
from urllib import parse
from flask import Request
from utils.decorators.authorized_client import authorized_client
from utils.decorators.validation import validate_put_file
from utils.exceptions import APIException
from .services import StorageService

@app.route('/storage/file', methods=['POST', 'DELETE'])
@authorized_client
@validate_put_file
def file_storage(request: Request):
    if request.method == 'POST':
        return __put_file(request)
    elif request.method == 'DELETE':
        return __delete_file(request)

def __put_file(request: Request):
    file = request.files['object']
    location = request.form['location'].strip()
    StorageService.put_file(file, parse.unquote(location))
    return 'OK'

def __delete_file(request: Request):
    object_location = (request.args.get('obj', '') or '').strip()
    if object_location == '':
        raise APIException('unknown_object_file', 400)
    StorageService.delete_file(object_location)
    return 'OK'