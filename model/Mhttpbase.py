#!/usr/bin/env python
# -*- coding:utf-8 -*-


import configparser
from schematics.models import Model
from schematics.types import StringType, URLType
from schematics.types.compound import MultiType,ListType
# BaseHttp类

class BaseHttp(Model):
    '''配置要测试接口服务器的ip、端口、域名等信息'''
    host = StringType(required=True)
    title = StringType(required=True)
    port = StringType(required=True)
    No = StringType(required=True)
    file = StringType()
    param = ListType(MultiType())
    data = MultiType()


