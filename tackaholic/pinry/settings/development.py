from pinry.settings import *

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'development.db'),
        #'NAME': '/home/ubuntu/srv/CMPE203-Group1/tackaholic/development.db',
    }
}

SECRET_KEY = 'fake-key'

AUTH_PROFILE_MODULE = 'users.Profile'
