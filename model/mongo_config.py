#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:46 PM
# software: PyCharm

import motor.motor_tornado
from common.config import MONGO_SETTINGS


class MongoDB:
    def __init__(self):
        connection = motor.motor_tornado.MotorClient("localhost", 27017)
        self.db = connection['project']
