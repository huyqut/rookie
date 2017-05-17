# XML parsing

from xml.dom import minidom
import xml.etree.ElementTree as et

path = './data/chap23_xml.xml'

file = minidom.parse(path)
giantList = file.getElementsByTagName('giant')
print(len(giantList))
for giant in giantList:
    uid = giant.getElementsByTagName('uid')[0]
    print(uid.firstChild.nodeValue)
    name = giant.getElementsByTagName('name')[0]
    print(name.firstChild.nodeValue)

area = file.getElementById('123')  # Does not work
print(area)

root: et.Element = et.parse(path).getroot()
area = root.find(".//area-1[@id='titan']")
print(area)
