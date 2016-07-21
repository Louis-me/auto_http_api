__author__ = 'Administrator'
def compare(exJson,factJson):
    if factJson["appStatus"]["errorCode"] == 0:
       return exJson==factJson
    else:
        print("接口请求失败")
        return False