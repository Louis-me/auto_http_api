__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import xlsxwriter
class xlsxwriterBase:
    def __init__(self, wd, data):
        self.wd = wd
        self.data = data
    def init(self, worksheet):
         # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)

        # worksheet.set_row(0, 200)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")
        # Create a new Chart object.

        worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
        worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
        worksheet.merge_range('A3:A6', '这里放图片', get_format_center(self.wd))

        _write_center(worksheet, "B3", '项目名称', self.wd)
        _write_center(worksheet, "B4", '接口版本', self.wd)
        _write_center(worksheet, "B5", '脚本语言', self.wd)
        _write_center(worksheet, "B6", '测试网络', self.wd)


        # data = {"test_name": "智商", "test_version": "v2.0.8", "test_pl": "android", "test_net": "wifi"}
        _write_center(worksheet, "C3", self.data['test_name'], self.wd)
        _write_center(worksheet, "C4", self.data['test_version'], self.wd)
        _write_center(worksheet, "C5", self.data['test_pl'], self.wd)
        _write_center(worksheet, "C6", self.data['test_net'], self.wd)

        _write_center(worksheet, "D3", "接口总数", self.wd)
        _write_center(worksheet, "D4", "通过总数", self.wd)
        _write_center(worksheet, "D5", "失败总数", self.wd)
        _write_center(worksheet, "D6", "测试日期", self.wd)



        # data1 = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}
        _write_center(worksheet, "E3", self.data['test_sum'], self.wd)
        _write_center(worksheet, "E4", self.data['test_success'], self.wd)
        _write_center(worksheet, "E5", self.data['test_failed'], self.wd)
        _write_center(worksheet, "E6", self.data['test_date'], self.wd)

        _write_center(worksheet, "F3", "分数", self.wd)


        worksheet.merge_range('F4:F6', '60', get_format_center(self.wd))

        pie(self.wd, worksheet)
    def test_detail(self, worksheet):

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



        worksheet.merge_range('A1:H1', '测试详情', get_format(self.wd, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
        _write_center(worksheet, "A2", '用例ID', self.wd)
        _write_center(worksheet, "B2", '接口名称', self.wd)
        _write_center(worksheet, "C2", '接口协议', self.wd)
        _write_center(worksheet, "D2", 'URL', self.wd)
        _write_center(worksheet, "E2", '参数', self.wd)
        _write_center(worksheet, "F2", '预期值', self.wd)
        _write_center(worksheet, "G2", '实际值', self.wd)
        _write_center(worksheet, "H2", '测试结果', self.wd)

        # data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
        #                   "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
        #                   "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
        #         "test_sum": 100,"test_success": 20, "test_failed": 80}
        temp = 3
        for item in self.data["info"]:
            _write_center(worksheet, "A"+str(temp), item["t_id"], self.wd)
            _write_center(worksheet, "B"+str(temp), item["t_name"], self.wd)
            _write_center(worksheet, "C"+str(temp), item["t_method"], self.wd)
            _write_center(worksheet, "D"+str(temp), item["t_url"], self.wd)
            _write_center(worksheet, "E"+str(temp), item["t_param"], self.wd)
            _write_center(worksheet, "F"+str(temp), item["t_hope"], self.wd)
            _write_center(worksheet, "G"+str(temp), str(item["t_actual"]), self.wd)
            _write_center(worksheet, "H"+str(temp), str(item["t_result"]), self.wd)
            temp = temp+1
    def close(self):
        self.wd.close()
def get_format(wd, option={}):
    return wd.add_format(option)

def get_format_center(wd,num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


 # 生成饼形图
def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
    'name':       '接口测试统计',
    'categories':'=测试总况!$D$4:$D$5',
   'values':    '=测试总况!$E$4:$E$5',
    })
    chart1.set_title({'name': '接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})




