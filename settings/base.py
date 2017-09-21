import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^7lk$)tv1j-r+^^4r5y_b+o!8(61sdx**48g!xnh(9^^&eb%$3'


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dd74b8c4.ngrok.io']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
)

AUTH_USER_MODEL = 'accounts.User'

SITE_URL = 'http://127.0.0.1'
PAYPAL_NOTIFY_URL = 'http://dd74b8c4.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<clairemitchell0509@gmail.com>'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
    'django_forms_bootstrap',
    'stripe',
    'paypal.standard.ipn',
    'debug_toolbar',
    'tinymce',
    'emoticons',
    'accounts',
    'paypal_store',
    'products',
    'magazines',
    'threads',
    'polls',

]

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailAuth',)
LOGIN_URL = '/login/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'auth_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'auth_demo.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static"),
)

TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", 'js', 'tinymce', 'tinymce.min.js')

STATIC_URL = '/static/'
STATIC_ROOT = ''