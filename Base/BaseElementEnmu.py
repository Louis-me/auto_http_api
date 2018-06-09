import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Element(object):
    INFO_FILE = PATH("../Log/info.pickle") # 记录结果
    REPORT_FILE = PATH("../Report/Report.xlsx") # 测试报告
    API_FILE = PATH("../Report/api.xlsx") # 用例文件
    PICT_PARAM = PATH("../Log/param.txt") # 写入pict需要的参数
    PICT_PARAM_RESULT = PATH("../Log/param_result.txt") # pict生成后的数据
    OPEN_PICT = PATH("../Setting/Config.ini") # 打开pict配置器

    ERROR_EMPTY = "error_empty"
    ERROR_VALUE = "error_value"