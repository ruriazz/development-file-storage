def manage_app(app):
    from utils import shutdown_session
    from utils import exceptions

    from modules.storage import handlers as __storage_route
    from modules.file import handlers as __file_route