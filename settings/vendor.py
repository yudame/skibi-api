import os

from settings import LOCAL

# STATIC FILES
if not LOCAL:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE


# AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
AWS_STORAGE_BUCKET_NAME = AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME', "")
AWS_OPTIONS = {
    'AWS_ACCESS_KEY_ID': AWS_ACCESS_KEY_ID,
    'AWS_SECRET_ACCESS_KEY': AWS_SECRET_ACCESS_KEY,
    'AWS_STORAGE_BUCKET_NAME': AWS_S3_BUCKET_NAME,
}
AWS_DEFAULT_ACL = 'public-read'
AWS_SNS_NAME = os.environ.get('AWS_SNS_NAME', "")
AWS_STATIC_URL = 'https://' + AWS_S3_BUCKET_NAME + '.s3.amazonaws.com/'


if not LOCAL:
    STATIC_URL = AWS_STATIC_URL

CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": os.environ.get('REDIS_URL'),
    }
}

FONTAWESOME_5_CSS = "//cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
# FONTAWESOME_5_CSS_ADMIN = None
# FONTAWESOME_5_ICON_CLASS = 'default'
# FONTAWESOME_5_PREFIX = 'fa'


# SENDINBLUE.COM EMAIL SERVICE
# ANYMAIL = {
#     # (exact settings here depend on your ESP...)
#     "SERVICE_API_KEY": SERVICE_API_KEY,
# }
# EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
DEFAULT_FROM_EMAIL = "info@example.com"  # if you don't already have this in settings
SERVER_EMAIL = "info@example.com"  # ditto (default from-email for Django errors)


# HEROKU DATABASE
import dj_database_url
DATABASES = {'default': dj_database_url.config(), }
# Set DATABASE_URL in config if using other host
# DATABASE_URL = f"postgresql://{username}:{password}@{host}:5432/{dbname}"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# OAUTH AND SOCIAL
SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', '')
SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_CLIENT_ID', '')  # client id
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_CLIENT_SECRET', '')
AUTH0_CALLBACK_URL = os.environ.get('AUTH0_CALLBACK_URL', '')
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]


# CLOUDINARY
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL', '')


# ANALYTICS STAGE
# MIXPANEL_API_TOKEN = os.environ.get('MIXPANEL_API_TOKEN')
# MIXPANEL_API_KEY = os.environ.get('MIXPANEL_API_KEY')
# MIXPANEL_API_SECRET = os.environ.get('MIXPANEL_API_SECRET')

# GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-1234567-8'
# FACEBOOK_PIXEL_ID = '1234567890'
# HUBSPOT_PORTAL_ID = '1234'
# HUBSPOT_DOMAIN = 'somedomain.web101.hubspot.com'
# INTERCOM_APP_ID = '0123456789abcdef0123456789abcdef01234567'
# OPTIMIZELY_ACCOUNT_NUMBER = '1234567'


PUSHOVER_USER_KEY = os.environ.get('PUSHOVER_USER_KEY', '')
PUSHOVER_API_TOKEN = os.environ.get('PUSHOVER_API_TOKEN', '')
