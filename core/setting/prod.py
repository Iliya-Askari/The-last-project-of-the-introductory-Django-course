from core.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a4xmzjuz44_6k+!l@=8y&+_@ef8oh#^6!g_^j)v4vrgpc-*@1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["*"]
SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'x8W82CEhzDjwaYwVivcnPdTP',
        'HOST': 'askari86',
        'PORT': 5432,
    }
}

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT= BASE_DIR / "static"
MEDIA_ROOT= BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]


## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

CSRF_COOKIE_SECURE = True

## X-Frame-Options

SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 
# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'