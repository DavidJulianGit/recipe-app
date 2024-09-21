import environ, os

from .base import *

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = [".herokuapp.com",".railway.app","localhost", "127.0.0.1", "0.0.0.0"]
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://127.0.0.1",
    "https://0.0.0.0",
    "https://recipe-app-production-7591.up.railway.app",
    "https://whispering-forest-79119-3ed907d805e9.herokuapp.com/"
]  

MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("DB_NAME"),
#         "USER": env.str("DB_USER"),
#         "PASSWORD": env.str("DB_PWD"),
#         "HOST": env.str("DB_HOST"),
#         "PORT": env.str("DB_PORT"),
#     }
# }

# If you want to use sqlite3 instead, then uncomment this and comment the above.

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
#}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dmmf1k2lve5ea",  # database name
        "USER": "u2qtl6qvrdscu4",  # database user
        "PASSWORD": "p9929f8f28da996d73df20eefd9c5dafff7ba67ba6706e399bf87184d12d5fc72",  # database password
        "HOST": "c3nv2ev86aje4j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}

#STATIC_ROOT = str(BASE_DIR / "staticfiles")
#STATICFILES_DIRS = (str(BASE_DIR / "static"),)

# Connect to our database remotely
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

import django_on_heroku

django_on_heroku.settings(locals())


#DATABASE_URL = env.str("DATABASE_URL")

#DATABASES = {
 #   "default": dj_database_url.config(default=DATABASE_URL),
#}