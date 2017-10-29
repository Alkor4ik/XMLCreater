from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8').decode('utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

group = Element('group')

for i in range(4):
    name = 'serv ' + str(i)
    ip = 'ip address server ' + str(i)

    server = SubElement(group, 'server')
    #server.text = 'This child contains text.'

    display_name = SubElement(server, 'display_name')
    display_name.text = name

    name_server = SubElement(server, 'name_server')
    name_server.text = ip

print(prettify(group))