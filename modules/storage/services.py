import os
from app import settings
from werkzeug.datastructures import FileStorage
from utils.exceptions import APIException

class StorageService:
    def put_file(file: FileStorage, location: str):
        directory = os.path.join(settings.UPLOAD_FOLDER, location)

        if not os.path.exists(directory):
            os.mkdir(directory)

        file.save(os.path.join(settings.UPLOAD_FOLDER, location, file.filename))

    def delete_file(object_location: str):
        object_location = os.path.join(settings.UPLOAD_FOLDER, object_location)

        if not os.path.exists(object_location):
            raise APIException('object_file_not_found', 400)

        os.remove(object_location)