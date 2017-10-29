

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8').decode('utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

group = Element('group')

for n in range(4):

    server = SubElement(group, 'server')

    display_name = SubElement(server, 'display name')
    display_name.text = 'Name Server'

    server_name = SubElement(server, 'server name')
    server_name.text = 'IP address'

print(prettify(group))
