__author__ = 'Administrator'
from objectpath import *

# hope = {"Data": [{"TypesId": "559", "Initials": "", "TypesName": "干货"}], "Total": "6", "Success": "1"}
# result = {
#     "Data": [{"TypesId": "111", "Initials": "", "TypesName": "干货"},
#              {"TypesId": "222", "Initials": "", "TypesName": "33"}],
#     "Total": "6", "Success": "0"}

def compareKey(obj):
    d_l = []
    if isinstance(obj, dict):
        for k in obj:
            d_l.append(k)
        return d_l
    else:
        return obj
# 两个list之前的差集，如果为[]说明就是无差集
def subtract(list_a, list_b):
    temp =list(set(list_a)-(set(list_b)))
    print(temp)
    if len(temp) > 0:
        return False
    else:
        return True
    # isList 返回数据中是否包含嵌套(data:[{n:1}])
def compareJson(hope, result, isList):
    hope_tree = Tree(hope)
    result_tree = Tree(result)
    if hope_tree.execute("$.Success") == result_tree.execute("$.Success"):
        if isList == "1":
            if(subtract(compareKey(hope_tree.execute("$.Data")[0]), compareKey(result_tree.execute("$.Data")[0]))):
                print("嵌套对比成功")
                return True
            else:
                print("嵌套对比失败")
                return False
        else:
            print("无嵌套")
            return True
    else:
        print("接口测试失败")
        return False
# if i_tree.execute("$.Success") == j_tree.execute("$.Success"):
#     if compareKey(j["Data"][0]) == compareKey(i["Data"][0]):
#         return True
#     else:
#         return False
# else:
#     print("对比失败")

    # def ordered(obj):
    # if isinstance(obj, dict):
    # return sorted((k, ordered(v)) for k, v in obj.items())
    #     if isinstance(obj, list):
    #         return sorted(ordered(x) for x in obj)
    #     else:
    #         return obj