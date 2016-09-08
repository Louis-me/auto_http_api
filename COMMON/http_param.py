__author__ = 'Administrator'
# 参数化请求
def str__post_param(list_param):
    result = {}
    for i in list_param:
        result[i["name"]] = i["value"]
    return result

def str_get_param(list_param, param):
    result = "?"
    result += list_param["name"] + "=" + list_param["value"] + "&"
    return str_sub(0, len(result)-1, result) + "&" + for_dict(param)

def for_dict(d):
    result = ""
    for (k, v) in d.items():
        result += str(k) + "=" + str(v)
    return result

def str_sub(start, end, str):
    return str[start:end]
