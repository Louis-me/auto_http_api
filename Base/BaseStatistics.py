import pickle


def readInfo(path):
    data = []
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
            print(data)
        except EOFError:
            data = []
            print("读取文件错误")
    print("------read-------")
    print(data)
    return data


def writeInfo(kw, path="data.pickle"):
    """
    :type data: dict
    """
    data = {"result": kw["result"], "hope": kw["hope"], "msg": kw["msg"], "url": kw["url"], "params": kw["params"]
             ,"code": kw["code"], "method": kw["method"], "res": kw['res']}
    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        pickle.dump(result, f)
