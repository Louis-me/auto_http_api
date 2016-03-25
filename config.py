#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
# 配置类
class ConfigHttp:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'}
    # 设置http头
    def set_header(self, headers):
        self.headers = headers
    # 封装HTTP GET请求方法
    def get(self, url, params):
        # params = urllib.parse.urlencode(params)
        url = "http://"+self.host+":"+self.port+url
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            # a = {}
            # dict.fromkeys(x for x in a if x in b)
            # print(r.text.find("TurnType"+":"+ "2"))
            return r.text
        except Exception:
            print('no json data returned')
            return {}
    # 封装HTTP POST请求方法,支持上传图片
    def post(self, url, data, files=None):
        data = eval(data)
        url = 'http://' + self.host + ':' + str(self.port)+url
        r =requests.post(url, files=files, data=data)
        print(data)
        json_response = r.text
        # print(json_response)
        return json_response