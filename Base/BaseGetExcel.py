import xlrd
import xlsxwriter
from Base.BaseElementEnmu import Element
from Base.BaseExcel import *
from Base.BaseStatistics import readInfo


def read_excel(file='c:/test.xls'):
    data = xlrd.open_workbook(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(0)  # one rows data
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                # row[i] = colnames[i] + row[i]
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def write_excel():
    workbook = xlsxwriter.Workbook(Element.REPORT_FILE)
    worksheet2 = workbook.add_worksheet("测试详情")
    operateReport = OperateReport(workbook)
    operateReport.detail(worksheet2, readInfo(Element.INFO_FILE))
    operateReport.close()

if __name__ == "__main__":
    pass