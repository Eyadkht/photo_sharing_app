from .base import *

# SECURITY WARNING: App Engine's security features ensure that it is safe to
# have ALLOWED_HOSTS = ['*'] when the app is deployed. If you deploy a Django
# app not on App Engine, make sure to set an appropriate host here.
# See https://docs.djangoproject.com/en/2.1/ref/settings/
ALLOWED_HOSTS = ['*']

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# Update the secret key to a value of your own before deploying the app.
SECRET_KEY = '2$geg+fmgd#rificatw1x8r1bloktbl*utc%z_qtczqt6-9qec'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Install PyMySQL as mysqlclient/MySQLdb to use Django's mysqlclient adapter
# See https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-db-api-drivers
# for more information

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/photosharingapp-staging:europe-west2:photosharingapp-staging-instance',
            'USER': 'photoadmin',
            'PASSWORD': 'test!@#$$',
            'NAME': 'photosharingapp_staging_db',
        }
}

#ALLOWED_HOSTS = ['localhost', '127.0.0.1', '188.166.110.206', 'tallyapp.me', 'www.tallyapp.me']
from google.oauth2 import service_account

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'photosharing_storage'