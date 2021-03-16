from Base.BaseRunner1 import ParametrizedTestCase
from Base.BaseGetExcel import read_excel
from Base.BaseReq1 import Config
from Base.BaseElementEnmu import Element
from Base.BaseIni import BaseIni


class ApiTest(ParametrizedTestCase):
    def test_api(self):
        ls = read_excel(Element.API_FILE)
        if BaseIni(Element.OPEN_PICT).read_ini():
            Config(self.sessions).config_req_pict(ls)
        else:
            Config(self.sessions).config_req(ls)

    @classmethod
    def setUpClass(cls):
        super(ApiTest, cls).setUpClass()
