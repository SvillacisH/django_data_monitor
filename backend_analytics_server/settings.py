from pathlib import Path
import os
import pymysql

# Configuración obligatoria para MySQL en producción
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()

# BASE_DIR definido como Path pero usado con os.path para compatibilidad total
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: DEBUG debe ser False en producción
DEBUG = False

# Dominios permitidos de Railway
ALLOWED_HOSTS = ['.up.railway.app', 'localhost', '127.0.0.1']

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-tu-clave-aqui")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Debe ir después de SecurityMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend_analytics_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend_analytics_server.wsgi.application"

# Base de Datos usando variables de entorno de Railway
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQLDATABASE'),
        'USER': os.environ.get('MYSQLUSER'),
        'PASSWORD': os.environ.get('MYSQLPASSWORD'),
        'HOST': os.environ.get('MYSQLHOST'),
        'PORT': os.environ.get('MYSQLPORT'),
    }
}

# Internacionalización
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS CORREGIDA ---
STATIC_URL = "static/"

# Donde Django busca los archivos en desarrollo (carpeta raíz /static)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Donde se recopilan para producción (Carpeta /assets)
# Usamos os.path.join para evitar el Warning de 'No directory at /app/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

# Almacenamiento optimizado pero menos estricto (mejor para debugging en Railway)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# --- FIN CONFIGURACIÓN ESTÁTICOS ---
API_URL = 'https://cimontes.pythonanywhere.com/landing/api/index/'

CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app",
    "https://*.app.github.dev",
    "https://localhost:8000",
    "http://127.0.0.1:8000"
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'