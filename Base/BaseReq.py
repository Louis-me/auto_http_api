import requests
import json
import ast
from Base.BaseElementEnmu import Element
from Base.BaseParams import  BaseFuzzParams
from Base.BaseStatistics import writeInfo

class Config(object):
    def __init__(self):
        pass

    def config_req(self, kw):
        app = {}
        header = {"Accept": "*/*", "Content-Type": "application/json;charset=utf-8"}
        for item in kw:
            url = "%s://%s" % (item["protocol"], item["url"])
            print("==请求url:%s" % url)
            print("==请求参数:%s" % item["params"])
            params = "{}"
            if item.get("params"):
                params = item["params"]
            if item["method"] == "get":
                res = requests.get(url, data=json.dumps(ast.literal_eval(params)), headers=header, verify=False)
            elif item["method"] == "post":
                res = requests.post(url, data=json.dumps(ast.literal_eval(params)), headers=header, verify=False)
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
            app["ress"] = res  # 传给检查函数进行解析

            app["result"] = self.__check(app["hope"], app["ress"])
            print("==响应码=:%s=" % app["code"])

            writeInfo(app, Element.INFO_FILE)

    def config_req_pict(self, kw, req=None):
        app = {}
        header = {"Accept": "*/*", "Content-Type": "application/json;charset=utf-8"}
        for item in kw:
            url = "%s://%s" % (item["protocol"], item["url"])
            # 如果有参数才做模糊测试，没有做正向场景测试
            if item.get("params"):
                print("进行逆向场景测试")
                params = BaseFuzzParams().param_fi(ast.literal_eval(item["params"]))
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
                    # app["hope"] = item.get("hope", "")
                    app["hope"] = ""
                    app["res"] = str(res.text)
                    app["result"] = ""
                    print("请求url:%s" % url)
                    print("请求参数:%s" % app["params"])
                    print("响应码:%s" % app["code"])
                    print("响应结果:%s" % app["res"])
                    writeInfo(app, Element.INFO_FILE)
                else:

                    self.config_req(kw)
    def __check(self, hope, res):
        resp = json.dumps(json.loads(res.text), separators=(',', ':'))
        is_check = 0  # 0表示期望值不存在，没有进行检查;1成功;-1失败
        hopes = hope.split("|")
        if len(hopes) and len(hope):
            is_check = 1
            # 循环检查期望值是否在实际值中能找到
            for j in hopes:
                if resp.find(j) == -1:
                    is_check = -1
                    break
        if is_check == 0:
            return "未检查"
        elif is_check == 1:
            return "成功"
        else:
            return "失败"
