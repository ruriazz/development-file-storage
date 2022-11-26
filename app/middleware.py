from werkzeug import Request, Response
from . import settings

class Middleware:
    def __init__(self, app):
        self._app = app

    def __call__(self, env, res):
        request = Request(env)
        response = Response(res)

        return self._app(env, res)
