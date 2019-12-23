#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:13 PM
# software: PyCharm

from handlers import FeedHandler, IndexHandler

url_patterns = [
    (r"^/feed$", FeedHandler),
    (r'^/$', IndexHandler)
]
