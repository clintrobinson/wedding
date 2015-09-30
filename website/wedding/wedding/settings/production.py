"""Production settings and globals."""


from os import environ

from settings_base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
	""" Get the environment setting or return exception """
	try:
		return environ[setting]
	except KeyError:
		error_msg = "Set the %s env variable" % setting
		raise ImproperlyConfigured(error_msg)


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = "dev@liftinteractive.com"
DEFAULT_FROM_EMAIL = SERVER_EMAIL
########## END EMAIL CONFIGURATION


########## POSTMARK CONFIGURATION
POSTMARK_API_KEY = 'a876b1f2-2144-4e0a-9dbb-6fc2f801a3ff'
POSTMARK_SENDER = 'dev@liftinteractive.com'
POSTMARK_TEST_MODE = DEBUG
########## END POSTMARK CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wedding',    # Or path to database file if using sqlite3.
        'USER': 'clint',             # Not used with sqlite3.
        'PASSWORD': '2fVgLSU38gGyUpE',     # Not used with sqlite3.
        'HOST': '',   # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                 # Set to empty string for default. Not used with sqlite3.
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## RAVEN
# RAVEN_CONFIG = {
#     'dsn': '',
# }
########## END RAVEN

try:
    from local_production import *
except ImportError:
    pass
