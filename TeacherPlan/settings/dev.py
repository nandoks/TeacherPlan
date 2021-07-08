from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': 'localhost',
    }
}

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

