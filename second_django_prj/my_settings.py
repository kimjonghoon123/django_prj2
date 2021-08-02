import os
import pymysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'django',
        'USER':  'root',
        'PASSWORD':  'whdgns1002@',
        'HOST': 'db',
        'PORT': '3306',
    }
}

SECRET_KEY = '^il&w&37030%c0kbg@9(h+k(jsps53_)brjyw)mksmj=*c^5vf'