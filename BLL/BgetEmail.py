__author__ = 'Administrator'
from COMMON import OperateFile as of
from DAL import DgetEmail

def read_email(Memail):
    if of.base_file(Memail.file, 'r').check_file():
        return DgetEmail.read_email(Memail)
    print(u"文件不存在")
    return ""