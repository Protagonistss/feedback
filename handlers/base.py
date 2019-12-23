#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:15 PM
# software: PyCharm

import tornado.web
from common.config import MONGO_SETTINGS
from tornado.gen import *


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.settings['db'][MONGO_SETTINGS['mongo']['db']]

    @property
    def log(self):
        return self.application.log

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    @coroutine
    def options(self):
        # no body
        self.set_default_headers()
        self.set_status(200)
        self.finish()
