#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:16 PM
# software: PyCharm

from handlers.base import BaseHandler
import tornado_swirl as swirl

swirl.describe(title='APIS', description='FeedBack APIS')


@swirl.restapi('/feed')
class FeedHandler(BaseHandler):
    async def get(self):
        """
            Returns user Profile

            200 Response:
                status(SuccessResponse) -- success
                msg(SuccessResponse) -- message
            :return:
        """
        await self.db.project.insert_one({'name': 'huangshan', 'age': 20})
        await self.finish({'status': '200', "msg": 'ok'})


class IndexHandler(BaseHandler):
    async def get(self):
        self.write("aaa")
