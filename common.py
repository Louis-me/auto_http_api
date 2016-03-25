__author__ = 'Administrator'

'''
对比子json是否在父json字符串中规则：
主json {'Data':[{a:b},{c:d}]}
副{a:b,c:d}
'''
def find_dict(parentJson, sonJson):
    for j in range(len(parentJson["Data"])):
      if parentJson["Data"][j] == sonJson:
        return True
    return False

# for j,data in enumerate(parentJson["Data"]):
#     if data == sonJson: return True
# for data in parentJson["Data"]
