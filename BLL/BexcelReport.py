__author__ = 'Administrator'
from DAL import DexcelReport

class  ExcelReport():
    def __init__(self,wd,data):
        self.wd = wd
        self.data = data
        self.excel = DexcelReport.ExcelReport(self.wd)

    def init(self, worksheet, data):
        self.excel.init(worksheet, data)

    def detail(self, worksheet, info):
        self.excel.test_detail(worksheet, info)
        self.close()

    def close(self):
        self.excel.close()