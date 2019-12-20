#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:15 PM
# software: PyCharm

import tornado.web
from common.config import MONGO_SETTINGS


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.settings['db'][MONGO_SETTINGS['mongo']['db']]

    @property
    def log(self):
        return self.application.log
