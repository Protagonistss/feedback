#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:16 PM
# software: PyCharm

from handlers.base import BaseHandler


class FeedHandler(BaseHandler):
    async def get(self):
        document = {'key': 'val'}
        result = await self.db.project.insert_one(document)
        await self.finish({"msg": 'ok'})


class IndexHandler(BaseHandler):
    async def get(self):
        self.write("aaa")
