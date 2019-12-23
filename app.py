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
from tornado_swirl.swagger import Application
from tornado_swirl import api_routes


class MyApplication(object):

    def __init__(self):
        self.initiate_app()

    def initiate_app(self):
        app = self.make_up()
        app.listen(options.port)

    def make_up(self):
        return Application(
            api_routes(),
            **settings
        )


def main():
    app = MyApplication()
    print("feedback is running on {}".format(options.port))
    tornado.ioloop.IOLoop.current().start()
    io_loop = tornado.ioloop.IOLoop.instance()


if __name__ == '__main__':
    main()
