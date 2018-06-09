__author__ = 'shikun'
import xlsxwriter
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperateReport:
    def __init__(self, wd):
        self.wd = wd

    def detail(self, worksheet, info):
        # 设置列行的宽高
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)
        worksheet.set_row(8, 30)

        worksheet.merge_range('A1:H1', '测试详情', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                    'valign': 'vcenter', 'bg_color': 'blue',
                                                                    'font_color': '#ffffff'}))
        _write_center(worksheet, "A2", '请求', self.wd)
        _write_center(worksheet, "B2", '方法', self.wd)
        _write_center(worksheet, "C2", '请求参数', self.wd)
        _write_center(worksheet, "D2", '请求说明', self.wd)
        _write_center(worksheet, "E2", '期望值', self.wd)
        _write_center(worksheet, "F2", '响应码 ', self.wd)
        _write_center(worksheet, "G2", '实际结果 ', self.wd)
        _write_center(worksheet, "H2", '是否通过 ', self.wd)

        temp = 3
        for item in info:
            # print(item)
            _write_center(worksheet, "A" + str(temp), item["url"], self.wd)
            _write_center(worksheet, "B" + str(temp), item["method"], self.wd)
            _write_center(worksheet, "C" + str(temp), item["params"], self.wd)
            _write_center(worksheet, "D" + str(temp), item["msg"], self.wd)
            _write_center(worksheet, "E" + str(temp), item["hope"], self.wd)
            _write_center(worksheet, "F" + str(temp), item["code"], self.wd)
            _write_center(worksheet, "G" + str(temp), item["res"], self.wd)
            _write_center(worksheet, "H" + str(temp), item["result"], self.wd)

            temp += 1

    def close(self):
        self.wd.close()


def get_format(wd, option={}):
    return wd.add_format(option)


# def link_format(wd):
#     red_format = wd.add_format({
#         'font_color': 'red',
#         'bold': 1,
#         'underline': 1,
#         'font_size': 12,
#     })
def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})


def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)


def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


def set_row(worksheet, num, height):
    worksheet.set_row(num, height)

    # 生成饼形图


def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
        'name': '自动化测试统计',
        'categories': '=测试总况!$C$4:$C$5',
        'values': '=测试总况!$D$4:$D$5',
    })
    chart1.set_title({'name': '测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})


if __name__ == '__main__':
    sum = {'testSumDate': '25秒', 'sum': 10, 'pass': 5, 'testDate': '2017-06-05 15:26:49', 'fail': 5,
           'appVersion': '17051515', 'appSize': '14M', 'appName': "'简书'"}
    info = [{"id": 1, "title": "第一次打开", "caseName": "testf01", "result": "通过", "phoneName": "三星"},
            {"id": 1, "title": "第一次打开",
             "caseName": "testf01", "result": "通过", "img": "d:\\1.PNG", "phoneName": "华为"}]
    workbook = xlsxwriter.Workbook('Report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    bc = OperateReport(wd=workbook)
    bc.init(worksheet, sum)
    bc.detail(worksheet2, info)
    bc.close()
    #
