__author__ = 'Administrator'
from COMMON.BaseGoals import Goals as go

# 参数化请求
class  chttp_params():
    def __init__(self):
        pass
     # post参数化
    def str__post_param(self, list_param):
        result = {}
        for i in list_param:
            if i["must"] == "1": # 如果参数是必填
                result[i["name"]] = self.str_to(i["type"], i["value"])
        return result
    # get 参数化，param是dict
    def str_get_param(self, dict_param, param):
        result = "?"
        if dict_param["must"] == "1": # 如果参数是必填
            result += dict_param["name"] + "=" + dict_param["value"] + "&"
        return self.str_sub(0, len(result)-1, result) + "&" + self.for_dict(param)
    # 合并dict
    def for_dict(self, d):
        result = ""
        for (k, v) in d.items():
            result += str(k) + "=" + str(v)
        return result
    # 截取str
    def str_sub(self, start, end, str):
        return str[start:end]
    # 转换类型
    def str_to(self, type, s):
        elements = {
        go.INT: lambda: int(s),
        go.STR: lambda: s,
        go.FLOAT: lambda: float(s)
        }
        return elements[type]()



