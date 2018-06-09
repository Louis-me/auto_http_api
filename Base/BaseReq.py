import requests
import json
import ast
from Base.BaseElementEnmu import Element
from Base.BaseParams import BaseParams
from Base.BaseStatistics import writeInfo

class Config(object):
    def __init__(self):
        pass

    def config_req(self, kw):
        app = {}
        header = {"Accept": "*/*", "Content-Type": "application/json;charset=utf-8"}
        for item in kw:
            url = "%s://%s" % (item["protocol"], item["url"])
            print("==请求url:%s==" % url)
            print("==请求参数:%s==" % item["params"])
            if item["method"] == "get":
                res = requests.get(url, data=json.dumps(ast.literal_eval(item["params"])), headers=header, verify=False)
            elif item["method"] == "post":
                res = requests.post(url, data=json.dumps(ast.literal_eval(item["params"])), headers=header, verify=False)
            else:
                print("现在只针post和ge方法进行了测试，其他方法请自行扩展")
            app["url"] = item["url"]
            app["method"] = item["method"]
            app["params"] = item["params"]
            app["code"] = str(res.status_code)
            app["msg"] = item["mark"]
            app["hope"] = item.get("hope", "")
            app["res"] = str(res.text)
            print("==响应结果=:%s=" % app["res"])

            app["result"] = self.__check(app["hope"], app["res"])
            print("==响应码=:%s=" % app["code"])

            writeInfo(app, Element.INFO_FILE)

    def config_req_pict(self, kw, req=None):
        app = {}
        header = {"Accept": "*/*", "Content-Type": "application/json;charset=utf-8"}
        for item in kw:
            url = "%s://%s" % (item["protocol"], item["url"])
            params = BaseParams().param_fi(ast.literal_eval(item["params"]))["params"]
            for i in params:
                _info = ""
                if i.get("info", "null") != "null":
                    _info = i.get("info", "参数正确")
                    i.pop("info")
                if item["method"] == "get":
                    res = requests.get(url, data=json.dumps(i), headers=header)
                else:
                    res = requests.post(url, data=json.dumps(i), headers=header)
                app["url"] = item["url"]
                app["method"] = item["method"]
                app["params"] = str(i)
                app["code"] = str(res.status_code)
                app["msg"] = item["mark"] + "_" + _info
                app["hope"] = item.get("hope", "")
                app["res"] = str(res.text)
                app["result"] = ""
                print("==请求url:%s==" % url)
                print("==请求参数:%s==" % app["params"])
                print("==响应码=:%s=" % app["code"])
                print("==响应结果=:%s=" % app["res"])
                writeInfo(app, Element.INFO_FILE)


    def __check(self, hope, res):
        hope = json.loads(hope)
        fact = json.loads(res)
        for items in fact:
            if type(fact[items]) == list:
                for item in fact[items]:
                    for k in hope:
                        if item.get(k, "") == hope[k]:
                            return "通过"
            if type(fact[items]) == dict:
                for k in hope:
                    if fact[items].get(k, "") == hope[k]:
                        return "通过"
            for k in hope:
                if fact.get(k, "") == hope[k]:
                    return "通过"
        return "失败"
