from .base import *  # noqa

CORS_ORIGIN_WHITELIST = []
SECURE_SSL_REDIRECT = True

# Disables the browseable API
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)
}

EMAIL_HOST = None
EMAIL_PORT = 587
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
EMAIL_USE_SSL = True
