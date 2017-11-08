# -*- coding: utf-8 -*-

import csv
import os
from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring
from xml.etree import ElementTree
from xml.dom import minidom

path = os.path.dirname(os.path.realpath(__file__))
path_file = os.path.join(path, "data\\result.xml")


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8').decode('utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


with open('testcsv.csv') as csvfile:  # Открываем файл с подготовленными именами машин и ip
    contentreader = csv.reader(csvfile, delimiter=';')
    test = Element('test')
    for row in contentreader:
        # print(row[0])

        group = SubElement(test, 'group')
        properties = SubElement(group, 'properties')
        expanded = SubElement(properties, 'expanded')
        expanded.text = 'False'
        name = SubElement(properties, 'name')
        name.text = row[0]

        servers = {
            'HV': 11,
            'DC': 13,
            'KSC': 15
        }
        for i in servers:
            server = SubElement(group, 'server')
            properties = SubElement(server, 'properties')
            displayName = SubElement(properties, 'displayName')
            name = SubElement(properties, 'name')
            name.text = row[1][:-4] + str(servers.get(i))
            displayName.text = row[0] + '-' + i

pretty_test = prettify(test)

print(pretty_test)
#print(tree.write("C:\\temp\\result.xml"))

# stout = BeautifulSoup(server, "xml").prettify()

# print(stout)
