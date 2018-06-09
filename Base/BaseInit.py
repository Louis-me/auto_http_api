from Base.BaseFile import BaseFile
from Base.BaseElementEnmu import Element


class BaseInit(object):
    def __init__(self):
        self.bf = BaseFile()

    def mk_file(self):
        self.__destroy()
        self.bf.mk_file(Element.INFO_FILE)
        self.bf.mk_file(Element.PICT_PARAM)
        self.bf.mk_file(Element.PICT_PARAM_RESULT)

    def __destroy(self):
        self.bf.remove_file(Element.INFO_FILE)
        self.bf.remove_file(Element.PICT_PARAM_RESULT)
        self.bf.remove_file(Element.PICT_PARAM)
