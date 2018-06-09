import configparser

'''
对ini文件的读写改
'''


class BaseIni(object):
    def __init__(self, path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path)

    def read_ini(self):
        _pict = self.cfg.get("default", "pict")
        return True if _pict.lower() == 'true' else False

    def __write_ini(self):
        self.cfg.add_section("default1")
        self.cfg.set("default1", "title", "test msg")
        self.cfg.set("default1", "id", "test msg")
        self.cfg.add_section("ematter")
        self.cfg.set("ematter", "pages", 250)
        self.cfg.write(open('1.ini', "w"))

    def __edit_ini(self):
        self.cfg.set("default", "pict", "True")
        self.cfg.write(open('1.ini', "r+"))

if __name__ == "__main__":
    from Base.BaseElementEnmu import Element
    t = BaseIni(Element.OPEN_PICT).read_ini()
    print(t)