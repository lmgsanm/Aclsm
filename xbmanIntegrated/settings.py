#-*- coding:utf-8 -*-
"""
Django settings for xbman-Integrated project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import absolute_import

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from celery.schedules import crontab
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ru-8hm+(=9y-&4990-j@20^kb!2bjnm05dsf_-o6*%ft06h=5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'kombu.transport.django',
    'Integrated',
    'loghunter',
    'asset',
    # 'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'xbmanIntegrated.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'xbmanIntegrated.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGIN_URL = '/login/'

SESSION_COOKIE_AGE = 60*60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

djcelery.setup_loader()

BROKER_URL = 'django://'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "templates/"),
)
AUTH_USER_MODEL = 'Integrated.UserProfile'


CELERYBEAT_SCHEDULE = {
    'add-every-1-seconds': {
        'task': 'loghunter.tasks.get_database',
        # 'schedule': crontab(minute=u'40', hour=u'17',),
        'schedule': timedelta(seconds=120),
    },
    'add-every-2-seconds': {
        'task': 'loghunter.tasks.get_soft',
        # 'schedule': crontab(minute=u'40', hour=u'17',),
        'schedule': timedelta(seconds=120),
    },
}
GRAPPELLI_INDEX_DASHBOARD = 'xbmanIntegrated.dashboard.CustomIndexDashboard'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
GRAPPELLI_ADMIN_TITLE='XBMAN管理后台'

#是否发送短信通知
Notice = True
#短信通知电话设置
p_number = '13500000000,13522222222'

#salt服务器设置
ipaddr = '10.10.5.150'
port = 22
username = 'root'
password = 'u1m9s0k8'