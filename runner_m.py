#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
from COMMON.BaseGoals import Goals as go
from COMMON import check

import xlsxwriter
from MODEL import Memail
from BLL import BgetEmail,BsendEmail
from BLL import BexcelReport as excel
from COMMON import operateXML as om
from BLL import Bhttpbase
from MODEL import Mhttpbase
from BLL import Bresult, BresultDetail
from MODEL import Mresult, MresultDetail
from COMMON import http_param
import json
import ast


mresult = Mresult.result()
mresult.info = []
def get_email():
    g_email = Memail.email()
    g_email.file = "D:\\app\\auto_http34_test\\email.ini"
    email = BgetEmail.read_email(g_email)
    return email

# 所有的逻辑参数处理
def str_param():
    return http_param.chttp_params()

# 测试报告的输出
def excel_report(wd, data, worksheet_init, worksheet_detail):
    ex = excel.ExcelReport(wd, data)
    ex.init(worksheet_init, data[0])
    ex.detail(worksheet_detail, data[1])

# 得到xml配置接口信息和http请求实体类
def get_api():
   return om.getXML("d:\\app\\auto_http34_test\\test4.xml", Mhttpbase.BaseHttp())

# 设置http请求实体类
def configHttp(httpbase):
   return Bhttpbase.ConfigHttp(httpbase)

gm = get_api()[0] #读取api_xml
httpbase = get_api()[1] #读取http参数


# 接口详情页的excel
def resultInfo(mresultinfo, **kwargs):
    return BresultDetail.resultInfo(mresultinfo, **kwargs)

# 接口初始页的excel
def result(mresult, **kwargs):
    return Bresult.result(mresult, **kwargs)

# 错误日志统计
def sum_test_data(flag):
    if flag:
        go.RESULT = 'Pass'
        go.SUCCESS_SUM += 1
    else:
        go.RESULT = 'Fail'
        go.ERROR_NUM += 1

# 测试用例(组)类
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, testName, hope, index):
        super(TestInterfaceCase, self).__init__(testName)
        self.hope = hope
        self.index = index
    def setUp(self):
        self.config_http = configHttp(httpbase)
    def function(self):
        temp_result = False
        hp = str_param()
        if self.index == 1: #第一个xml预留的主要是登陆
             if gm[self.index]["method"] == "POST":
                go.REALLY_RESULT = self.config_http.post(url=gm[self.index]["url"], params=hp.str__post_param(gm[self.index]["param"]))
                if go.REALLY_RESULT.get("status_code") == 200:
                    hope = ast.literal_eval(self.hope)
                    temp_result = check.compare(hope, go.REALLY_RESULT)
                    if temp_result:
                        go.LOGIN_KEY = gm[self.index]["login"]
                        print(go.LOGIN_KEY)
                        go.LOGIN_VALUE = go.REALLY_RESULT["content"][0][go.LOGIN_KEY]
                else:
                    pass
        else:
            if gm[self.index]["login"] != "0":
                    go.PARAMS[go.LOGIN_KEY] = go.LOGIN_VALUE # 登陆成功后返回过来的值，可能是token,userid等
            if gm[self.index]["method"] == "POST":
                go.PARAMS = hp.str__post_param(gm[self.index]["param"])
                go.REALLY_RESULT = self.config_http.post(gm[self.index]["url"], go.PARAMS)
            if gm[self.index]["method"] == "GET":
                go.PARAMS = hp.str_get_param(gm[self.index]["param"][0], go.PARAMS) #把登陆成功后的token,userid合并到请求参数中
                go.REALLY_RESULT = self.config_http.get(gm[self.index]["url"], go.PARAMS)
            hope = ast.literal_eval(self.hope)
            temp_result = check.compare(hope, go.REALLY_RESULT,  gm[self.index]["isList"])

        sum_test_data(temp_result) #统计
        go.CASE_TOTAL += 1

# 获取测试套件
def get_test_suite(index):
    test_suite = unittest.TestSuite()
    hope = gm[index]["hope"] # 预期值
    test_suite.addTest(TestInterfaceCase("function", hope, index))
    return test_suite

# 运行测试用例函数
def run_case(runner):
    case_list = httpbase.No
    case_list = ast.literal_eval(case_list)  # 把字符串类型的list转换为list
    if len(case_list) == False: #判断是否执行指定的用例ID
        temp_case = gm
        for index in range(1, len(temp_case)):
            test_suite = get_test_suite(index)
            runner.run(test_suite)
            # 记录运行结果
            mresult.info.append(json.loads(json.dumps(resultInfo(MresultDetail.resultInfo(), t_id=gm[index]["id"], t_name=gm[index]["name"], t_url=gm[0]["host"] +"/" + gm[index]["url"],
                       t_param=str(go.PARAMS), t_actual=go.REALLY_RESULT, t_hope=gm[index]["hope"], t_result=go.RESULT,
                       t_method=gm[index]["method"]).to_primitive())))
    else:
        for i in case_list:
            for j in range(1, len(gm)):
                if str(i) == gm[j]['id']:
                    test_suite = get_test_suite(j)
                    runner.run(test_suite)
                    # 记录运行结果
                    mresult.info.append(json.loads(json.dumps(resultInfo(MresultDetail.resultInfo(), t_id=gm[j]["id"], t_name=gm[j]["name"], t_url=gm[0]["host"] +"/"+gm[j]["url"],
                       t_param=str(go.PARAMS), t_actual=go.REALLY_RESULT, t_hope=gm[j]["hope"], t_result=go.RESULT,
                       t_method=gm[j]["method"]).to_primitive())))

# 运行测试套件
if __name__ == '__main__':
    start_time = time.time()
    runner = unittest.TextTestRunner()
    run_case(runner)
    end_time = time.time()
    sum_time = "%.2f" % (end_time - start_time)

    # 测试报告
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    data = json.loads(json.dumps(result(mresult, test_date=str(sum_time) + "毫秒", test_sum=go.CASE_TOTAL, test_failed=go.ERROR_NUM, test_version="v2.2", test_pl="python3",
    test_net="本地连接", test_name=gm[0]["title"], test_success=go.SUCCESS_SUM, info=mresult.info)))
    excel_report(workbook, data, worksheet, worksheet2)

    # 发送email
    # get_email = get_email()
    # BsendEmail.send_mail(get_email)


