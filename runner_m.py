#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time

from controller import config
import htmlreport
from model.common import Goals as go
from controller import con_api_xml
from controller import check

gm = con_api_xml.ret_xml() # 读取xml
hb = con_api_xml.ret_http_base(gm) #读取http参数


#初始化报告
html_report1 = htmlreport.HtmlReport(gm)

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
                print(go.REALLY_RESULT)
                hope = eval(self.hope)
                # temp = testJson.compareJson(hope, go.REALLY_RESULT, gm[self.index]["isList"])
                temp = check.compare(hope,go.REALLY_RESULT)
                if temp:
                    go.LOGIN_KY = gm[1]["login"]
                    go.LOGIN_VALUE = go.REALLY_RESULT["content"][0][go.LOGIN_KY]
                    go.RESULT = 'Pass'
                    html_report1.success_num = html_report1.success_num + 1
                else:
                    go.RESULT = 'Fail'
                    html_report1.error_num = html_report1.error_num + 1
        else:
            if gm[self.index]["login"] != "0":
                    go.PARAMS[go.LOGIN_KEY] = go.LOGIN_VALUE
            if gm[self.index]["method"] == "POST":
                response = self.config_http.post(go.URL, go.PARAMS)
            if gm[self.index]["method"] == "GET":
                response = self.config_http.get(go.URL, go.PARAMS)
            print(type(response))
            go.REALLY_RESULT = eval(str(response))
            hope = eval(self.hope)
            # temp = testJson.compareJson(hope, go.REALLY_RESULT, gm[self.index]["isList"])
            temp = check.compare(hope,go.REALLY_RESULT,  gm[self.index]["isList"])
            print(temp)
            if temp:
                go.RESULT = 'Pass'
                html_report1.success_num = html_report1.success_num + 1
            # except AssertionError:
            else:
                go.RESULT = 'Fail'
                html_report1.fail_num = html_report1.fail_num + 1
# 获取测试套件
def get_test_suite(index):
    test_suite = unittest.TestSuite()
    hope = gm[index]["hope"] # 预期值
    # print(hope)
    test_suite.addTest(TestInterfaceCase("function", hope,index))
    return test_suite

# 运行测试用例函数
def run_case(runner):
    print("11111")
    html_report1.case_total = 0
    case_list = hb.No
    case_list = eval(case_list)  # 把字符串类型的list转换为list
    html_report1.case_list = case_list
    temp_case = ""
    if len(case_list) == False: #判断是否执行指定的用例ID
        temp_case = gm
        for index in range(1, len(temp_case)):
            go.URL = gm[index]['url']
            go.PARAMS = gm[index]["params"]
            test_suite = get_test_suite(index)
            runner.run(test_suite)
            # 记录运行结果
            gm[index]["result"] = go.RESULT
            gm[index]["really_result"] = go.REALLY_RESULT
    else:
        for i in case_list:
            for j in range(1, len(gm)):
                if str(i) == gm[j]['id']:
                    go.URL = gm[j]['url']
                    go.PARAMS = gm[j]["params"]
                    test_suite = get_test_suite(j)
                    runner.run(test_suite)
                    gm[j]["result"] = go.RESULT
                    gm[j]["really_result"] = go.REALLY_RESULT
# 运行测试套件
if __name__ == '__main__':
    start_time = time.time()
    runner = unittest.TextTestRunner()
    run_case(runner)
    end_time = time.time()
    html_report1.time_caculate(end_time - start_time)  # 计算测试消耗时间
    html_report1.generate_html( r'D:\\app\\auto_http34_test\\report\report.html')     # 生成测试报告

