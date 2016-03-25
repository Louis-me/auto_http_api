#!/usr/bin/env python
# -*- coding:utf-8 -*-
import httpbase
import unittest
import time
import config
import htmlreport
import operateXML
import common
import testJson
header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0' }

#读取xml接口测试信息
gm = operateXML.getXML("test3.xml")
# 读取并配置接口服务器IP，端口等信息
base_http = httpbase.BaseHttp(gm)
#初始化报告
html_report1 = htmlreport.HtmlReport(gm)

# 定义结构体
class DataStruct:
    '''于接收excel读取的测试数据,记录要写入测试报告的数据'''
    pass
test_data = DataStruct()
test_data.url = ''               # 接收接口url
test_data.params = {}            # 接收接口参数
test_data.result = 'Fail'       # 接收测试结果
test_data.really_result = ""
test_data.login_key = ""
test_data.login_value=""
# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, testName, hope, index):
        super(TestInterfaceCase, self).__init__(testName)
        self.hope = hope
        self.index = index
    def setUp(self):
        self.config_http = config.ConfigHttp(base_http.get_host(), base_http.get_port())
    def function(self):
        response = ""
        if self.index == 1:
             if gm[self.index]["method"] == "POST":
                response = self.config_http.post(test_data.url, test_data.params)
                test_data.really_result = eval(response)

                hope = eval(self.hope)
                temp = testJson.compareJson(hope, test_data.really_result, gm[self.index]["isList"])
                if temp:
                    test_data.login_key = test_data.really_result["login"]
                    test_data.login_value = test_data.really_result[test_data.login_key]
                    test_data.result = 'Pass'
                    html_report1.success_num = html_report1.success_num + 1
                else:
                    test_data.result = 'Fail'
                    html_report1.error_num = html_report1.error_num + 1
        else:
            if gm[self.index]["login"] != "0":
                    test_data.params[test_data.login_key] = test_data.login_value
            if gm[self.index]["method"] == "POST":
                response = self.config_http.post(test_data.url, test_data.params)
            if gm[self.index]["method"] == "GET":
                response = self.config_http.get(test_data.url, test_data.params)
            test_data.really_result = eval(response)
            hope = eval(self.hope)
            temp = testJson.compareJson(hope, test_data.really_result, gm[self.index]["isList"])
            print("----------")
            print(temp)
            if temp:
                test_data.result = 'Pass'
                html_report1.success_num = html_report1.success_num + 1
            # except AssertionError:
            else:
                test_data.result = 'Fail'
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
    html_report1.case_total = 0
    case_list = base_http.get_NO()
    case_list = eval(case_list)  # 把字符串类型的list转换为list
    html_report1.case_list = case_list
    temp_case = ""
    if len(case_list) == False: #判断是否执行指定的用例ID
        temp_case = gm
        for index in range(1, len(temp_case)):
            test_data.url = gm[index]['url']
            test_data.params = gm[index]["params"]
            test_suite = get_test_suite(index)
            runner.run(test_suite)
            # 记录运行结果
            gm[index]["result"] = test_data.result
            gm[index]["really_result"] = test_data.really_result
    else:
        for i in case_list:
            for j in range(1, len(gm)):
                if str(i) == gm[j]['id']:
                    test_data.url = gm[j]['url']
                    test_data.params = gm[j]["params"]
                    test_suite = get_test_suite(j)
                    runner.run(test_suite)
                    gm[j]["result"] = test_data.result
                    gm[j]["really_result"] = test_data.really_result
# 运行测试套件
if __name__ == '__main__':
    start_time = time.time()
    runner = unittest.TextTestRunner()
    run_case(runner)
    end_time = time.time()
    html_report1.time_caculate(end_time - start_time)  # 计算测试消耗时间
    html_report1.generate_html( r'd:\\report.html')     # 生成测试报告

