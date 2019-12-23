#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/23 12:47 PM
# software: PyCharm
from tornado_swirl.swagger import schema


@schema
class SuccessResponse:
    """
    Properties:
        status(str) -- Required
        msg(str) -- Required
    """
    Status = 'status'
    Msg = 'msg'
