# -*- coding: utf-8 -*-
"""
Django settings for onedollar_backend project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from collections import OrderedDict

from django.utils.translation import ugettext_lazy as _

import stripe

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b-3qh07ezr4l2dj@&b$g%xgpaszo!9w*!d9(l-!*!s0hnwyha='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_countries',
    'rest_framework',
    'rest_framework.authtoken',
    'password_reset',
    'notifications',
    'constance',
    'import_export',
    'django_tables2',
    'multiselectfield',
    'django_admin_listfilter_dropdown',

    "categories",
    "categories.editor",

    'unify_django',
    'django_crontab',

    'onedollar',
    'shopapp',
    'merchants',
)

CRONJOBS = [
    ('* * * * *', 'onedollar.models.second_chance_4h_48h', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('*/30 * * * *', 'onedollar.models.before_the_draw_30_min', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * * * *', 'onedollar.models.enter_his_address_after_8h_48h', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * * * *', 'onedollar.models.collect_your_cash_4h_24h', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * * * *', 'onedollar.models.pns_free_daily_cat', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * * * *', 'onedollar.models.pns_spin_cat_uncage', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('0 */4 * * *', 'onedollar.models.pns_uncage_cat_remind', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('0 9 * * *', 'onedollar.models.pns_uncage_cat_remind_after_1day', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * 1 * *', 'shopapp.api.PaymentMerchant', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('0 4 1 * *', 'shopapp.api.Decode', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('* * 16 * * *','shopapp.api.PaymentMerchant', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
    ('0 4 16 * * *','shopapp.api.Decode', '>> /webapps/onedollar_backend/logs/cron.log 2>&1'),
]

CONSTANCE_CONFIG = OrderedDict([ 
    ('THE_FREE_CREDITS_GIVEN', (2, _('Number of free credits given for new user'), int)),
    ('LIMIT_NUMBER_OF_PAYMENT_PER_DAY', (2, _('Limit number of payment per day'), int)),
    ('REWARD_VALUE', (5, _('Reward value'), float)),
    ('HIDE_WON_PRODUCT', (7, _('Hide won product after (day)'), int)),
    ('LIMIT_AMOUT_OF_PAYMENT_PER_WEEK', (40, _('Limit amount of payment per week ($)'), int)),
    ('REFERRAL_AMOUNT', (2, _('Free $ given to new referral (only) on top of The FREE credits given'), int)),
    ('REFERRAL_SMS', ('Join me on One Dollar and get $5 to spend. Use my referral link to download the app: ###url###', _('Referral SMS, please keep the placeholder "###url###" which will be replace with the referral URL'))),
    ('QUOTE_1', ('', _('Quote #1'))),
    ('QUOTE_2', ('', _('Quote #2'))),
    ('QUOTE_3', ('', _('Quote #3'))),
    ('QUOTE_4', ('', _('Quote #4'))),
    ('QUOTE_5', ('', _('Quote #5'))),
    ('QUOTE_6', ('', _('Quote #6'))),
    ('QUOTE_7', ('', _('Quote #7'))),
    ('QUOTE_8', ('', _('Quote #8'))),
    ('QUOTE_9', ('', _('Quote #9'))),
    ('QUOTE_10', ('', _('Quote #10'))),
    ('STRIPE_ERROR_MSG_INSUFFICIENT_FUND', ('Your card has insufficient fund', '')),
    ('STRIPE_ERROR_MSG_DECLINED', ('Your card was declined', '')),
    ('STRIPE_ERROR_MSG_INCORRECT', ('Your card number is incorrect', '')),
    ('STRIPE_ERROR_MSG_NOTSUPPORT', ('Your card doesn\'t support this type of purchase', '')),
    ('STRIPE_ERROR_MSG_RISKY', ('Stripe blocked this card as too risky', '')),
    ('FIVE_STARS_RATING', (False, 'Checked to display 5 stars rating reward', bool)),
    ('GIVE_5_GET_5', (False, 'Checked to display give 5 get 5 reward', bool)),
    ('SHARE_YOUR_IDEA', (False, 'Checked to display share your idea reward', bool)),
    ('INSTALL_APPS_TITLE', ('Earn everyday - install new app', '')),
    ('INSTALL_APPS_DESCRIPTION', ('Discover new game, a new app crafted for you. Earn your $ daily.', '')),
    ('INSTALL_APPS_REWARD', (15, u'Reward for install app (¢)', int)),
    ('REFERRAL_TOPUP_REQUIRE', (5, 'Amount required to topup to get referral reward', int)),
    ('REFERRAL_TOPUP_REWARD', (5, 'Referral reward', int)),
    ('AUTO_SHARE_TO_FB_FANPAGE', (False, 'Auto share to FB fanpage', bool)),
    ('TEXT_WARNING_FRAUD', ('Stop! You are fraud!!!', '')),
    ('TEXT_FIND_OUT_MORE', ('Earn dollar coins rewards and spend them in the WIN section to get luxurious product for $1', '')),
    ('TEXT_HEADER_SHOP', ('SHOP', '')),
    ('TEXT_HEADER_CART', ('CART', '')),
    ('TEXT_HEADER_BET', ('TAP TO WIN', '')),
    ('TEXT_CART_MISSED', ('Your tickets', '')),
    ('TEXT_CART_WON', ('Congratulations', '')),
    ('TEXT_CART_BET', ('Your tickets', '')),
    ('TEXT_SHARE', ('Share your ideas and earn', '')),
    ('TEXT_SHARE_DESCRIPTION', ('Every month $25 are given away to the 5 best suggestions', '')),
    ('TEXT_SHARE_URL', ('https://fb.com/', '')),
    ('TEXT_DRAW_DESCRIPTION', ('You can see when the draw will happen. No go back and bet again.', '')),
    ('TEXT_HELPTEXT_SHOP_INTRO', ('Buy any product and get your Dollar Coins rewards instanlty to keep playing. Delivery is always FREE.', '')),
    ('TEXT_HELPTEXT_BET_INTRO', ('You have $%d. Buy tickets with your Dollar Coins, wait for the draws to see the winners. Delivery is always FREE', '')),
    ('TEXT_HELPTEXT_ORDER_HISTORY_INTRO', ('For every dollars spend you get rewards. Use your rewards in the CLUB product.', '')),
    ('TEXT_GAME_TITLE', ('You bet.You get a lucky to spin. Spin it to collect coin and claim super discount', '')),
    ('TEXT_GAME_HELPTEXT_TITLE', ('Here is title of helptext game', '')),
    ('TEXT_GAME_HELPTEXT_TEXT', ('Here is texts of helptext game', '')),
    ('REQUIRE_COINS_1', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_2', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_3', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_4', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_5', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_6', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_7', (60, _('Require coins ($)'), int)),
    ('REQUIRE_COINS_8', (60, _('Require coins ($)'), int)),
    ('DISCOUNT_1', (10, _('Discount (%)'), int)),
    ('DISCOUNT_2', (10, _('Discount (%)'), int)),
    ('DISCOUNT_3', (10, _('Discount (%)'), int)),
    ('DISCOUNT_4', (10, _('Discount (%)'), int)),
    ('DISCOUNT_5', (10, _('Discount (%)'), int)),
    ('DISCOUNT_6', (10, _('Discount (%)'), int)),
    ('DISCOUNT_7', (10, _('Discount (%)'), int)),
    ('DISCOUNT_8', (10, _('Discount (%)'), int)),
    ('DISCOUNT_TIME_1', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_2', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_3', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_4', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_5', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_6', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_7', (30, _('Discount time (min)'), int)),
    ('DISCOUNT_TIME_8', (30, _('Discount time (min)'), int)),
    ('DAILY_WIN_MIN', (0, _('Mini cat win range (coins)'), int)),
    ('DAILY_WIN_MAX', (100, _('Mini cat win range (coins)'), int)),
    ('CLAIM_WIN_MIN', (0, _('Mini cat win range (coins)'), int)),
    ('CLAIM_WIN_MAX', (100, _('Mini cat win range (coins)'), int)),
    ('TIME_UNCAGE', (240, _('Mini cat time uncage (240 minutes = 4 hours)'), int)),
    ('TIME_DAILY', (240, _('Mini cat time daily (240 minutes = 4 hours)'), int)),
])

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': ('THE_FREE_CREDITS_GIVEN', 'LIMIT_NUMBER_OF_PAYMENT_PER_DAY','REWARD_VALUE','HIDE_WON_PRODUCT',
                        'LIMIT_AMOUT_OF_PAYMENT_PER_WEEK','REFERRAL_AMOUNT','REFERRAL_SMS',
                        'QUOTE_1','QUOTE_2','QUOTE_3','QUOTE_4','QUOTE_5','QUOTE_6','QUOTE_7',
                        'QUOTE_8','QUOTE_9','QUOTE_10','STRIPE_ERROR_MSG_INSUFFICIENT_FUND',
                        'STRIPE_ERROR_MSG_DECLINED','STRIPE_ERROR_MSG_INCORRECT',
                        'STRIPE_ERROR_MSG_NOTSUPPORT','STRIPE_ERROR_MSG_RISKY',
                        'FIVE_STARS_RATING','GIVE_5_GET_5','SHARE_YOUR_IDEA','REFERRAL_TOPUP_REQUIRE',
                        'INSTALL_APPS_TITLE','INSTALL_APPS_DESCRIPTION','INSTALL_APPS_REWARD',
                        'REFERRAL_TOPUP_REWARD','AUTO_SHARE_TO_FB_FANPAGE','TEXT_FIND_OUT_MORE','TEXT_WARNING_FRAUD','TEXT_HEADER_SHOP','TEXT_HEADER_CART',
                        'TEXT_HEADER_BET','TEXT_CART_MISSED','TEXT_CART_WON','TEXT_CART_BET',
                        'TEXT_SHARE','TEXT_SHARE_DESCRIPTION','TEXT_SHARE_URL','TEXT_DRAW_DESCRIPTION',
                        'TEXT_HELPTEXT_SHOP_INTRO','TEXT_HELPTEXT_BET_INTRO','TEXT_HELPTEXT_ORDER_HISTORY_INTRO',),
    'Game Config': ('TEXT_GAME_TITLE','TEXT_GAME_HELPTEXT_TITLE','TEXT_GAME_HELPTEXT_TEXT',
                    'DAILY_WIN_MIN','DAILY_WIN_MAX','CLAIM_WIN_MIN','CLAIM_WIN_MAX','TIME_UNCAGE','TIME_DAILY'),
    'Game Level 1': ('REQUIRE_COINS_1','DISCOUNT_1','DISCOUNT_TIME_1'),
    'Game Level 2': ('REQUIRE_COINS_2','DISCOUNT_2','DISCOUNT_TIME_2'),
    'Game Level 3': ('REQUIRE_COINS_3','DISCOUNT_3','DISCOUNT_TIME_3'),
    'Game Level 4': ('REQUIRE_COINS_4','DISCOUNT_4','DISCOUNT_TIME_4'),
    'Game Level 5': ('REQUIRE_COINS_5','DISCOUNT_5','DISCOUNT_TIME_5'),
    'Game Level 6': ('REQUIRE_COINS_6','DISCOUNT_6','DISCOUNT_TIME_6'),
    'Game Level 7': ('REQUIRE_COINS_7','DISCOUNT_7','DISCOUNT_TIME_7'),
    'Game Level 8': ('REQUIRE_COINS_8','DISCOUNT_8','DISCOUNT_TIME_8'),
}

FB_FANPAGE_ACCESS_TOKEN = 'EAAJLbDrTBuoBACDJQciJuQff1kYcgMZBoiSaL4wFgqCpGZAMjDbMShhsGHaoaGtxUN'+\
    'ZA0IPJQ0q7iiaRgBQpimXnk252qPlna88vYzbpWrYM9udUhT7SctuCr9ZBDuzGJDbmgY1CnZCB4XqqoZA4LbkWFaEwKEWWYZD'

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

ROOT_URLCONF = 'onedollar_backend.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['onedollar/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },

]

TEMPLATES_DIRS =(os.path.join(BASE_DIR,'templates','static'))

WSGI_APPLICATION = 'onedollar_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SITE_URL = 'http://localhost:8888/'
SITE_URL = 'https://dailywashbackend.herokuapp.com/'

STATIC_URL = SITE_URL + 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = SITE_URL + 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

AUTH_USER_MODEL = 'onedollar.OneDollarUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    'PAGE_SIZE': 10,
    'PAGINATE_BY': 10,  # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100  # Maximum limit allowed when using `?page_size=xxx`.
}

PARSE_APPLICATION_ID = 'ljefge6kqyjxZ6EuWaqpD7s8c4faoUfnjUYKrUwz'
PARSE_REST_API_KEY = 'ng8xnDh5tje3PvlQkZAg7Nv2hjeybLClyX7VXmQ0'

# PAYPAL_MODE = 'live'   # live
# PAYPAL_CLIENT_ID = 'AfrsxX50AnUfdXa1OxhTDXPWTJPI2AA5W7JRHKhmHD74jaHgYTO6QGE2gFTVgUqgELkB_A7BOYwNTrvh'
# PAYPAL_CLIENT_SECRET = 'EBzA0zDHrJV7JimH6uzFX7PfPi5Te2q46dH6d2kSnCtsF48E2fpWSeCzbtWkn8h1zOkN2HLPY0tqxHkE'

PAYPAL_MODE = 'sandbox'   # sandbox
PAYPAL_CLIENT_ID = 'AeCm4dQQ9g_FhZqprRlojK4xcyr6epcxHa7nP0eokX2T0NyJO2ToS6bdz-9IY1Gl6O1NJjlpgFphlkZi'
PAYPAL_CLIENT_SECRET = 'EMl51LxwHmVn-KjhU-v7P4fscYKFerjdIU1u2wVXJDG4XTTCoGdls7aQ7YhEtim_huuEoYSJQZ6-gHoP'

STRIPE_KEYS = {
  'SECRET_KEY': 'sk_test_I7SCyltdAdzB0SPuwrphs27D',
  'PUBLISHABLE_KEY': 'pk_test_TJX4Fo6Cw8e4vPc8Lh9merQ7'
}
stripe.api_key = STRIPE_KEYS['SECRET_KEY']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

EMAIL_FROM = 'noreply@onedollarapp.biz'

COUNTRIES_ONLY = ['SG', ]

PERCENT_CLAIM_PAYOUT = 0.8
DATE_CLAIM_MONEY_AFTER = 21
DATE_DISPLAY_PRODUCT_AFTER = 160

FOURSQUARE_CLIENT_ID = 'ZPCMMIHKOID2FWWCULIAQKBFI1JA3LMTQFXH3ZYU2KEE5YOC'
FOURSQUARE_CLIENT_SECRET = 'JPWGI1R5T22TQ3YAIRHSAREUISAUCMI2QT2LFOWSCAJX5SPU'

ONEDOLLAR_BIZ_URL = 'http://onedollar.giinger.com/'
# ONEDOLLAR_BIZ_URL = 'http://onedollarapp.biz/'

ANDROID_CLIENT_ID = '26835176988-bafn42hjv6aagkan9rbqmujjpgq17ea6.apps.googleusercontent.com'
IOS_CLIENT_ID = '26835176988-on4ob5dqbm5s2jgrrsrcpj7qg5bo06rd.apps.googleusercontent.com'
WEB_CLIENT_ID = '26835176988-3n06vhhjglr58p7cola5v6rf5inbg7tn.apps.googleusercontent.com'

REDISKEYS_STRIPE_ERR = 'stripe_errors'

# try:
#     from settings_local import *
# except ImportError as e:
#     print e
