from core.settings import *



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a4xmzjuz44_6k+!l@=8y&+_@ef8oh#^6!g_^j)v4vrgpc-*@1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['example.com', 'www.example.com', '127.0.0.1', 'localhost']
ALLOWED_HOSTS = []

SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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



