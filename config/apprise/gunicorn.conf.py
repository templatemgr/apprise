# -*- coding: utf-8 -*-
import os
import multiprocessing

raw_env = [
    'LANG={}'.format(os.environ.get('LANG', 'en_US.UTF-8')),
    'DJANGO_SETTINGS_MODULE=core.settings',
]

pythonpath = 'REPLACE_WWW_ROOT_DIR'

bind = [
    '0.0.0.0:REPLACE_SERVER_PORT',
]

workers = int(os.environ.get(
    'APPRISE_WORKER_COUNT', multiprocessing.cpu_count() * 2 + 1))

timeout = int(os.environ.get('APPRISE_WORKER_TIMEOUT', 300))

worker_class = 'gevent'

max_requests = 1000
max_requests_jitter = 50

errorlog = '-'
accesslog = '-'
loglevel = 'warn'
