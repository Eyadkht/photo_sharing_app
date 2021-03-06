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

is_proxy = False

if is_proxy:
    #cloud_sql_proxy.exe -instances=photosharingapp-261121:europe-west2:photosharing-instance=tcp:3306
    #cloud_sql_proxy.exe -instances=photosharingapp-staging:europe-west2:photosharingapp-staging-instance=tcp:3306
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'NAME': 'photosharingapp_db',
                'USER': 'photoadmin',
                'PASSWORD': 'test!@#$$',
            }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'