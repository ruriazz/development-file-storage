from os import environ as env
from pathlib import Path

BASEPATH: str = Path(__file__).resolve().parent.parent
DEV_HOST: str = env.get('DEV_HOST', '127.0.0.1')
DEV_POST: str = env.get('DEV_POST', '8080')
ENV: str = env.get('ENV', 'development')
SECRET_KEY: str = env.get('SECRET_KEY', '6f2beeba3439545c8fb56d77232e608b1965acecfe45c5604a29da116787cf11')
DEBUG: bool = env.get('DEBUG', '1') == '1'
TESTING: bool = env.get('TESTING', '1') == '1'

TZ: str = env.get('TZ', 'UTC')

X_AUTH_KEY: str = env.get('X_AUTH_KEY', '4mJjjnHe-tK9GloCCF-kC_0nYcgBIVTDeMSUGwoOVb4') # use secrets.token_urlsafe(32)

UPLOAD_FOLDER: str = env.get('UPLOAD_FOLDER', 'storage')
DISALLOWED_MIMETYPE_UPLOAD: list = [i.strip() for i in env.get('DISALLOWED_MIMETYPE_UPLOAD', '').split(',')] + ['text/html']