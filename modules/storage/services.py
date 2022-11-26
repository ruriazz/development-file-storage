import os
from app import settings
from werkzeug.datastructures import FileStorage
from utils.exceptions import APIException

class StorageService:
    def put_file(file: FileStorage, location: str):
        store_location = os.path.join(settings.UPLOAD_FOLDER, location)

        directory = settings.UPLOAD_FOLDER
        for subdir in location.split('/'):
            directory = os.path.join(directory, subdir)
            if not os.path.exists(directory):
                os.mkdir(directory)

            try:
                file.save(os.path.join(settings.BASEPATH, store_location, file.filename))
                break
            except Exception as err:
                print(f"[ERROR] {err}")
                continue

    def delete_file(object_location: str):
        object_location = os.path.join(settings.UPLOAD_FOLDER, object_location)

        if os.path.exists(object_location):
            os.remove(object_location)