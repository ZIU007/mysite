"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n5e2^7m$jh_6x%!g4$w^6!7l!@03a4@0&41g2cf1m=f@jh8(a2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'ziu',
        'PASSWORD': 'ziu123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 发送邮件设置
# https://docs.djangoproject.com/en/2.0/ref/settings/#email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '1176417778@qq.com'
EMAIL_HOST_PASSWORD = 'silowsuivxpgggcb'  # 授权码
EMAIL_SUBJECT_PREFIX = '[Cybathlon_ZIU的博客] '
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)