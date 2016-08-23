#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
from controller import config
from model.common import Goals as go
from controller import con_api_xml
from controller import check
import BaseExcelReport as be
import xlsxwriter
import sendMail as sd
gm = con_api_xml.ret_xml() # 读取xml
hb = con_api_xml.ret_http_base(gm) #读取http参数
data = {"info":[]}
#初始化报告
# html_report1 = htmlreport.HtmlReport(gm)

# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, testName, hope, index):
        super(TestInterfaceCase, self).__init__(testName)
        self.hope = hope
        self.index = index
    def setUp(self):
        self.config_http = config.ConfigHttp(hb.host, hb.port)
    def function(self):
        response = ""
        if self.index == 1:
             if gm[self.index]["method"] == "POST":
                response = self.config_http.post(go.URL, go.PARAMS)
                go.REALLY_RESULT = eval(response)
                hope = eval(self.hope)
                # temp = testJson.compareJson(hope, go.REALLY_RESULT, gm[self.index]["isList"])
                temp = check.compare(hope, go.REALLY_RESULT)
                if temp:
                    go.LOGIN_KY = gm[1]["login"]
                    go.LOGIN_VALUE = go.REALLY_RESULT["content"][0][go.LOGIN_KY]
                    go.RESULT = 'Pass'
                    go.SUCCESS_SUM += 1
                else:
                    go.RESULT = 'Fail'
                    go.ERROR_NUM += 1
        else:
            if gm[self.index]["login"] != "0":
                    go.PARAMS[go.LOGIN_KEY] = go.LOGIN_VALUE
            if gm[self.index]["method"] == "POST":
                response = self.config_http.post(go.URL, go.PARAMS)
            if gm[self.index]["method"] == "GET":
                response = self.config_http.get(go.URL, go.PARAMS)
            go.REALLY_RESULT = eval(str(response))
            hope = eval(self.hope)
            # temp = testJson.compareJson(hope, go.REALLY_RESULT, gm[self.index]["isList"])
            temp = check.compare(hope, go.REALLY_RESULT,  gm[self.index]["isList"])
            if temp:
                go.RESULT = 'Pass'
                go.SUCCESS_SUM += 1
            # except AssertionError:
            else:
                go.RESULT = 'Fail'
                go.ERROR_NUM += 1
        go.CASE_TOTAL += 1

# 获取测试套件
def get_test_suite(index):
    test_suite = unittest.TestSuite()
    hope = gm[index]["hope"] # 预期值
    test_suite.addTest(TestInterfaceCase("function", hope,index))
    return test_suite

# 运行测试用例函数
def run_case(runner):
    case_list = hb.No
    case_list = eval(case_list)  # 把字符串类型的list转换为list
    temp_case = ""
    if len(case_list) == False: #判断是否执行指定的用例ID
        temp_case = gm
        for index in range(1, len(temp_case)):
            info = {}
            go.URL = gm[index]['url']
            go.PARAMS = gm[index]["params"]
            test_suite = get_test_suite(index)
            runner.run(test_suite)
            # 记录运行结果
            info["t_id"] = gm[index]["id"]
            info["t_name"] = gm[index]["name"]
            info["t_url"] = gm[0]["host"] + gm[index]["url"]
            info["t_param"] = gm[index]["params"]
            info["t_actual"] = go.REALLY_RESULT
            info["t_hope"] = gm[index]["hope"]
            info["t_result"] = go.RESULT
            info["t_method"] = gm[index]["method"]
            data["info"].append(info)
    else:
        for i in case_list:
            for j in range(1, len(gm)):
                if str(i) == gm[j]['id']:
                    info = {}
                    go.URL = gm[j]['url']
                    go.PARAMS = gm[j]["params"]
                    test_suite = get_test_suite(j)
                    runner.run(test_suite)
                    info["t_id"] = gm[j]["id"]
                    info["t_name"] = gm[j]["name"]
                    info["t_url"] = gm[0]["host"] + gm[j]["url"]
                    info["t_param"] = gm[j]["params"]
                    info["t_actual"] = go.REALLY_RESULT
                    info["t_hope"] = gm[j]["hope"]
                    info["t_result"] = go.RESULT
                    info["t_method"] = gm[j]["method"]
                    data["info"].append(info)
# 运行测试套件
if __name__ == '__main__':
    start_time = time.time()
    runner = unittest.TextTestRunner()
    run_case(runner)
    end_time = time.time()
    sum_time = "%.2f" % (end_time - start_time)
    data["test_date"] = str(sum_time) + "毫秒"
    data["test_sum"] = go.CASE_TOTAL
    data["test_failed"] = go.ERROR_NUM
    data["test_version"] = "v2.0.8"
    data["test_pl"] = "python 3"
    data["test_net"] = "本地连接"
    data["test_name"] = gm[0]["title"]
    data["test_success"] = go.SUCCESS_SUM

    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    # data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
    #                    "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
    #                    "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
    #          "test_sum": 100,"test_success": 20, "test_failed": 80, "test_name": "智商", "test_version": "v2.0.8", "test_pl": "android", "test_net": "wifi", "test_date": "2018-10-10 12:10"}

    bc = be.xlsxwriterBase(wd=workbook, data=data)
    bc.init(worksheet)
    bc.test_detail(worksheet2)
    bc.close()

    sd.send_mail("report.xlsx", ["284772894@qq.com", "ashikun@126.com"])


