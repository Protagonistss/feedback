#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 3:22 PM
# software: PyCharm

from __future__ import unicode_literals
import inspect, os

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
LOG_PATH = SITE_ROOT + "/log/"

MONGO_SETTINGS = {
    'mongo': {
        'host': 'localhost',
        'port': 27017,
        'db': 'feedback',
    },
}

FCGI_SETTIGNS = {
    'fcgi_port': 1024,
}

API_VERSION = 'v1'
