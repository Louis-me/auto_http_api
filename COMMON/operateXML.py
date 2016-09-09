__author__ = 'Administrator'
from xml.etree import ElementTree as ET

def getXML(xml, mhttp):
    tree  = ET.parse(xml)
    root = tree.getroot()
    i_base = {}
    interfaceName = []
    i_base["title"] = mhttp.title = root.find("title").text
    i_base["host"] = mhttp.host = root.find("host").text
    i_base["port"] = mhttp.port = root.find("port").text
    i_base["No"] = mhttp.No = root.find("No").text
    mhttp.header = root.find("header").text
    interfaceName.append(i_base)
    for elem in root.findall("InterfaceList"):
        i_app = {"param":[]}
        i_app["id"] = elem.find('id').text
        i_app["name"] = elem.find('name').text
        i_app["method"] = elem.find('method').text
        i_app["url"] = elem.find('url').text
        i_app["hope"] = elem.find('hope').text
        i_app["login"] = elem.find('login').text
        i_app["isList"] = elem.find('isList').text
        # interfaceName.append(i_app)
        for p in elem.findall("params"):
            param = {}
            param["name"] = p.find("name").text
            param["type"] = p.find("name").attrib.get("type")
            param["value"] = p.find("value").text
            param["must"] = p.find("must").text
            i_app["param"].append(param)
        interfaceName.append(i_app)
    # print(interfaceName)
    return interfaceName, mhttp
