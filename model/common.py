__author__ = 'Administrator'
class Goals(object):
    URL = ''               # 接收接口url
    PARAMS = {}            # 接收接口参数
    RESULT = 'Fail'       # 接收测试结果
    REALLY_RESULT = ""
    LOGIN_KEY = ""
    LOGIN_VALUE = ""
    SUCCESS_SUM = 0
    ERROR_NUM = 0
    CASE_TOTAL = 0
    HEADER = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'}