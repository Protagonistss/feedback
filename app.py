#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:09 PM
# software: PyCharm

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from urls import url_patterns
from settings import settings
from tornado_swirl.swagger import Application
from tornado_swirl import api_routes
from common import web_log

class MyApplication(object):

    def __init__(self):
        self.initiate_app()
        web_log.init()


    def initiate_app(self):
        app = self.make_up()
        app.listen(options.port)

    def make_up(self):
        return Application(
            api_routes(),
            url_patterns,
            **settings,
        )


def main():
    app = MyApplication()
    print("feedback is running on {}".format(options.port))
    tornado.ioloop.IOLoop.current().start()
    io_loop = tornado.ioloop.IOLoop.instance()


if __name__ == '__main__':
    main()
