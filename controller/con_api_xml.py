__author__ = 'Administrator'
from controller import operateXML
from model import httpbase


def ret_xml():
    gm = operateXML.getXML('test3.xml')
    return gm


def ret_http_base(gm):
    # print(gm[0]["host"])
    hb = httpbase.BaseHttp({"host": gm[0]["host"], "title": gm[0]["title"], "port": gm[0]["port"], "No": gm[0]["No"]})
    return hb
