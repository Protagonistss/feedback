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
from model import mongo
from common import web_log
from tornado_swirl.swagger import Application, describe
from tornado_swirl import api_routes


class MyApplication(object):

    def __init__(self):
        # self.db = mongo_config.MongoDB()
        # tornado.web.Application.__init__(self, url_patterns, **settings)
        self.initiateApp()

    def initiateApp(self):
        app = self.make_up()
        app.listen(9888)
        pass

    def make_up(self):
        return Application(
            api_routes(),
            **settings
        )


def main():
    app = MyApplication()
    # http_serve = tornado.httpserver.HTTPServer(app)
    # http_serve.listen(options.port)
    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()
    io_loop = tornado.ioloop.IOLoop.instance()


if __name__ == '__main__':
    main()
