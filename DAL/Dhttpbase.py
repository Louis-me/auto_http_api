__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import requests
import ast
import json

class ConfigHttp():
    def __init__(self, mhttpbase):
        self.mhttpbase = mhttpbase
    def get(self, url, params):
        result = {}
        url = "http://" + self.mhttpbase.host + ":" + self.mhttpbase.port + "/" + url + params
        print(url)
        r = requests.get(url, headers=ast.literal_eval(self.mhttpbase.header))
        r.encoding = 'UTF-8'
        if r.status_code == 200:
            result = json.loads(r.text)
        result["status_code"] = r.status_code
        print(result)
        return result

    # 封装HTTP POST请求方法,支持上传图片
    def post(self, url, files=None, data=None):
        url = 'http://' + self.mhttpbase.host + ':' + self.mhttpbase.port + "/" + url
        print(url)
        r = requests.post(url, files=files, data=data)
        result = {}
        if r.status_code == 200:
            result = json.loads(r.text)
        result["status_code"] = r.status_code
        print(result)
        return result