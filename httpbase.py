#!/usr/bin/env python
# -*- coding:utf-8 -*-


import configparser

# BaseHttp类
class BaseHttp:
    '''配置要测试接口服务器的ip、端口、域名等信息'''

    def __init__(self, gm):
      self.gm = gm

    # def set_host(self):
    #     self.host = self.gm["host"]

    def get_title(self):
        self.title = self.gm[0]["title"]

    def get_host(self):
        return self.gm[0]["host"]

    def set_port(self):
        self.port = self.gm[0]["port"]

    def get_port(self):
        return self.gm[0]['port']
    #获取指定接口id
    def get_NO(self):
        return self.gm[0]["No"]
