__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import requests
import json
class ConfigHttp():
    def __init__(self, mhttpbase):
        self.mhttpbase = mhttpbase
    def get(self, url, params):
        url = "http://" + self.mhttpbase.host + ":" + self.mhttpbase.port + "/" + url + params
        print(url)
        try:
            r = requests.get(url, headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'})
            r.encoding = 'UTF-8'
            return r.text
        except Exception:
            print('no json data returned')
            return {}
    # 封装HTTP POST请求方法,支持上传图片
    def post(self, url, files=None, data=None):
        # data = eval(data)
        url = 'http://' + self.mhttpbase.host + ':' + self.mhttpbase.port + "/" + url
        r =requests.post(url, files=files, data=data)
        json_response = r.text
        print(json_response)
        return json_response