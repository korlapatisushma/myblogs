"""
Django settings for myblogs project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_PATH=os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =os.getenv('SECRET_KEY','e1p2vbe!lbl0*yvk#+0ry61r02hkh&0i6i!@xg8&(nh*qhjlo9')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =os.getenv('DEBUG',True)
#DEBUG=False
ALLOWED_HOSTS = ['*']

#CSRF_TRUSTED_ORIGINS = ["https://myposts.azurewebsites.net/","https://myposts.azurewebsites.net/"]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1.apps.App1Config',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblogs.urls'
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
CSRF_TRUSTED_ORIGINS=["https://myposts-web.azurewebsites.net/","https://myposts-web.azurewebsites.net"]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ 
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WSGI_APPLICATION = 'myblogs.wsgi.application'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
'''DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME','myposts'),
        'USER': os.getenv('USER','ram'),
        'PASSWORD': os.getenv('PASSWORD','triveni@521'),
        'HOST': os.getenv('HOST','myposts-db.mysql.database.azure.com'),
        'PORT': os.getenv('PORT',3306),    
    }}'''


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True   

USE_TZ = True
#LOGIN_REDIRECT_URL = "home"
#LOGOUT_REDIRECT_URL = "home"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/ram/'
STATIC_ROOT=BASE_DIR / "ram"
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR / 'media/'
LOGIN_REDIRECT_URL='/'
# Base url to serve media files
MEDIA_URL = '/media/'

 #Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

'''DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
DEFAULT_FILE_STORAGE = 'ss.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'ss.custom_azure.AzureStaticStorage'
STATIC_LOCATION = "static"
MEDIA_LOCATION = "images"
AZURE_ACCOUNT_NAME=os.getenv('AZURE_ACCOUNT_NAME','myposts')
AZURE_ACCOUNT_KEY=os.getenv('AZURE_ACCOUNT_KEY','1wYTBkKwlU8S1apnS74x50V5+a8SHi/cqU0i5ZaxJZcWByS3A8HlHmOtzQ127Qppp8rVQ5PEHfni+AStjZgb1g==')
AZURE_CONTAINER=os.getenv('AZURE_CONTAINER','ramblob')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'  '''