from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1URLx914YWI0EgBoUgFr3COE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_k5mTHdMFNHuD5NmgTTmsjFuk')

# Paypal environment variables
SITE_URL = 'codeinstitutesocial-staging'
PAYPAL_NOTIFY_URL = 'codeinstitutesocial-staging.heroku.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<your PayPal merchant>