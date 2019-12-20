#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:09 PM
# software: PyCharm

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from settings import settings
from urls import url_patterns
from model import mongo_config
from common import web_log


class AppApplicationHandler(tornado.web.Application):

    def __init__(self):
        # self.db = mongo_config.MongoDB()
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = AppApplicationHandler()
    http_serve = tornado.httpserver.HTTPServer(app)
    http_serve.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
