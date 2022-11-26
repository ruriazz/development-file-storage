from http.client import HTTPException
import json
from flask import Flask, request

from . import settings
from .manager import manage_app
from .middleware import Middleware

app = Flask(__name__)

app.config.from_object(settings)
app.wsgi_app = Middleware(app.wsgi_app)

manage_app(app=app)