#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os

from img.pyh import *


class HtmlReport:
    def __init__(self, gm):
        self.filename = ''                   # 结果文件名
        self.time_took = '00:00:00'         # 测试耗时
        self.success_num = 0                  # 测试通过的用例数
        self.fail_num = 0                     # 测试失败的用例数
        self.error_num = 0                    # 运行出错的用例数
        self.case_list = []                   # 只运行部分用例模式下，存放运行过的用例所在行索引
        self.gm = gm
    # 生成HTML报告
    def generate_html(self, file):
        page = PyH(self.gm[0]["title"])
        page << h1(self.gm[0]["title"], align='center')
        page << p('测试总耗时：' + self.time_took)
        page << p('测试用例数：' + str(self.success_num+self.error_num) + '&nbsp'*10 + '成功用例数：' + str(self.success_num) +
                  '&nbsp'*10 + '失败用例数：' + str(self.fail_num)  +  '&nbsp'*10 + '出错用例数：' + str(self.error_num))
        tab = table( border='1', cellpadding='1', cellspacing='0', cl='table')
        tab1 = page << tab
        tab1 << tr(td('用例ID', bgcolor='#ABABAB', align='center') +
                   td('接口名称', bgcolor='#ABABAB', align='center') + td('接口协议', bgcolor='#ABABAB', align='center') +
                   td('URL', bgcolor='#ABABAB', align='center') + td('参数/数据', bgcolor='#ABABAB', align='center') +
                    td('实际值', bgcolor='#ABABAB', align='center') +  td('预期值', bgcolor='#ABABAB', align='center')+
                    td('测试结果', bgcolor='#ABABAB', align='center'))
        if len(self.case_list) == 0:
            for index in range(1, len(self.gm)):
                tab1<< tr(td(int(self.gm[index]["id"]), align='center') + td(self.gm[index]["name"]) +
                          td(self.gm[index]["method"]) + td(self.gm[index]["url"], align='center') +
                          td(self.gm[index]["params"], style='word-break:break-all') + td(self.gm[index]["really_result"]) +td(self.gm[index]["hope"], style='word-break:break-all')+
                            td(self.gm[index]["result"], align='center'))
        else:
            for i in self.case_list:
                for j in range(1, len(self.gm)):
                    if str(i) == self.gm[j]['id']:
                        tab1<< tr(td(int(self.gm[j]["id"]), align='center') + td(self.gm[j]["name"]) +
                                td(self.gm[j]["method"]) + td(self.gm[j]["url"], align='center') +
                                td(self.gm[j]["params"],style='word-break:break-all') + td(self.gm[j]["really_result"]) + td(self.gm[j]["hope"],style='word-break:break-all')+
                                td(self.gm[j]["result"], align='center'))
        self._set_result_filename(file)
        page.printOut(self.filename, 'UTF-8')
    # 设置结果文件名
    def _set_result_filename(self, filename):
        self.filename = filename
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % filename)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext
    # 统计运行耗时
    def time_caculate(self,seconds):
        self.time_took = "%.2f" %seconds
        return self.time_took
