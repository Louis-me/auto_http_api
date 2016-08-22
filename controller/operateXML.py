__author__ = 'Administrator'
from xml.etree import ElementTree as ET

def getXML(xml):
    """
    """
    tree  = ET.parse(xml)
    root = tree.getroot()
    i_base = {}
    interfaceName = []
    i_base["title"] = root.find("title").text
    i_base["host"] = root.find("host").text
    i_base["port"] = root.find("port").text
    i_base["No"] = root.find("No").text
    interfaceName.append(i_base)
    for elem in root.findall("InterfaceList"):
        i_app = {}
        i_app["id"] = elem.find('id').text
        i_app["name"] = elem.find('name').text
        i_app["method"] = elem.find('method').text
        i_app["url"] = elem.find('url').text
        i_app["params"] = elem.find('params').text
        i_app["hope"] = elem.find('hope').text
        i_app["login"] = elem.find('login').text
        i_app["isList"] = elem.find('isList').text
        interfaceName.append(i_app)
    # print(interfaceName)
    return interfaceName
