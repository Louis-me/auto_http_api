import uuid
from allpairspy import AllPairs
# pip install allpairspy

from collections import OrderedDict


class BaseFuzzParams(object):
    """ 设置接口的逆向参数
        自动生成模糊接口参数第一步，提前准备逆向场景
        Args:
            d: dict类型，正向接口参数
        Returns:
           dict
        Raises:
           无
        """

    def __get_data(self, d):
        data = {}
        for i in d:
            data[i] = []
            #  加入一般规则
            data[i].append({"info": "正确的值", "code": 1, "value": d[i], "key": i})
            data[i].append({"info": "为空", "code": -1, "value": "", "key": i})
            data[i].append({"info": "错误的值", "code": -2, "value": self.__param_format(type(d[i])), "key": i})
            data[i].append({"info": "删除", "code": -3, "key": i})
        # 加入其它规则：如路径遍历，xss，注入
        return data

    '''
    生成逆向场景参数
    '''

    def __param_format(self, key):
        if key == str:
            return str(uuid.uuid1())
        elif key == int:
            return 963852 # 也可以使用随机整数的方式
        elif key == list:
            return [str(uuid.uuid1())]
        elif key == dict:
            return {}
        elif key == "inject":
            return "t'exec master..xp_cmdshell 'nslookup www.google.com'--"
        # 路径遍历
        elif key == "path_traversal":
            pass
        else:
            return "null"

    '''
    得到逆向场景参数后，用AllPairs生成全对偶参数
    '''

    def __set_fuzz(self, d):
        data = []
        for i, par in enumerate(AllPairs(OrderedDict(d))):
            app = []
            for j in par:
                app.append(j)
            data.append(app)

        dd = []
        for i in data:
            d = []
            for j in range(len(i)):
                d.append(i[j])
            dd.append(d)

        d2 = []
        for i in dd:
            d1 = []
            for j in i:
                app = {}
                if j.get("code", -9) == -1:
                    app[j["key"]] = ""
                elif j.get("code", -9) == -3:
                    pass
                else:
                    app[j["key"]] = j["value"]
                app["info"] = j["key"] + j["info"]
                d1.append(app)
            d2.append(d1)
        return d2
    '''
    对外的函数，处理生成的对偶场景接口参数
     Returns:
           [{},{}]
    '''
    def param_fi(self, d):
        g_data = self.__get_data(d)
        s_fuzz = self.__set_fuzz(g_data)
        data = []
        for i in s_fuzz:
            for j in range(len(i)):
                _info = ""
                for k in range(len(i)):
                    _info = _info + "," + i[k]["info"]
                    i[0].update(i[k])
                i[0]["info"] = _info.strip(",")
                data.append(i[0])
                break
        return data
if __name__ == "__main__":
    fz = BaseFuzzParams().param_fi({"user": "name", "id": 1001, "pwd": "!@#$^&*", "data": {"test": "hello"}, "my_list":["1", "2"]})
    print(fz)