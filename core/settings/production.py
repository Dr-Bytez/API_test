from .base import *

###################################################################
# CORS
###################################################################

CORS_ALLOWED_ORIGINS = [
    'http://154.194.53.191:4555',
    'http://localhost:5173',
    'https://kingdesignn.ru',
    "http://localhost",
    "https://localhost",
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    'https://kingdesignn.ru',
    'http://kingdesignn.ru',
    'https://kingdesignn.ru/*',
    'http://154.194.53.191',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]