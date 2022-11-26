import os, magic
from app import settings
from flask import send_file
from utils.exceptions import APIException
from http.client import BAD_REQUEST

class FileService:
    def read_file(object_location: str):
        object_location = os.path.join(settings.BASEPATH, settings.UPLOAD_FOLDER, object_location)

        if not os.path.exists(object_location):
            raise APIException('object_not_found', BAD_REQUEST)

        mime = magic.Magic(mime=True)
        return send_file(object_location, mime.from_file(object_location))