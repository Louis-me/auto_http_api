import os
import uuid
import time
from Base.BaseFile import BaseFile
from Base.BaseElementEnmu import Element


class BaseParams():
    def __init__(self):
        pass

    def __get_error(self, kw):
        '''
        :param kw: dict|{"type":"error","info":"test"}
        :return:
        '''
        element = {
            Element.ERROR_EMPTY: lambda: "%s删除参数" % kw["info"],
            Element.ERROR_VALUE: lambda: "%s参数错误" % kw["info"]
        }
        return element[kw["type"]]()

    # 给外部调用已经处理好的接口参数
    def param_fi(self, param):
        bpp = {}
        bf = BaseFile()
        for k in param:
            _para = self.__param_format(param[k])
            bpp[k] = [
                {"%s:%s:%s:error:%s" % (k, k, _para, Element.ERROR_VALUE)},
                {"%s:%s:%s:error:%s" % (k, k, "", Element.ERROR_EMPTY)}
            ]
            _t_value = ""
            for j in bpp[k]:  # 处理参数，写入到文件中，给pict执行做准备
                v = str(j)
                value = v[2:len(v) - 2]
                _t_value = _t_value + value + ","
            bf.write(Element.PICT_PARAM, _t_value[0:len(_t_value) - 1])
        self.__pict_wire()
        time.sleep(2)
        pict_param = self.__read_pict_param()
        o_param = self.__filter_pict_param(param, pict_param)
        bf.remove_file(Element.PICT_PARAM)
        bf.remove_file(Element.PICT_PARAM_RESULT)
        bf.mk_file(Element.PICT_PARAM)
        bf.mk_file(Element.PICT_PARAM_RESULT)
        return o_param

    # pict生成接口参数
    def __pict_wire(self):
        cmd = "pict " + Element.PICT_PARAM + ">" + Element.PICT_PARAM_RESULT
        print(cmd)
        os.popen(cmd)

    # 读取pict已经生成的参数，并处理
    def __read_pict_param(self):
        result = []
        _result = BaseFile().read(Element.PICT_PARAM_RESULT)
        for i in range(1, len(_result)):
            v = _result[i][0].split(",")
            s = []
            for j in v:
                app = {}
                _j = j.split(":")
                if len(_j) == 5:
                    app["info"] = self.__get_error({"type": _j[4], "info": _j[0]})
                else:
                    app["info"] = self.__get_error({"type": _j[3], "info": _j[0]})
                    app[_j[0]] = _j[1]
                s.append(app)
            result.append(s)
        return result

        # 处理读取pict参数，处理好参数发请求

    def __filter_pict_param(self, ls, pict_param):
        _result = {"params": []}
        for item in pict_param:
            _info = ""
            _app = {}
            for i in item:
                for key in i:
                    if key == "info":
                        _info = _info + i["info"] + ","
                    else:
                        _app[key] = i[key]
                    _app["info"] = _info
            _result["params"].append(_app)
        ls["info"] = "全部参数正确"
        _result["params"].append(ls)

        return _result

    def __param_format(self, key):
        param_type = {
            str: lambda: str(uuid.uuid1()),
            list: lambda: [],
            # int: lambda: int(uuid.uuid1()),
            dict: lambda: {}
        }
        return param_type[type(key)]()


if __name__ == '__main__':
    at = BaseParams()
    # at.__get_error()
