"""
Settings for the tests.
"""

SECRET_KEY = 'dummy secret key'  # nosec

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'organizations',
    'tahoe_figures_plugins',
]

FEATURES = {}

MIDDLEWARE = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
