
from xml.etree import ElementTree

with open('Abilene-Topo-10-04-2004.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter() :
    print(node.tag, node.attrib, node.text)

with open('TM-2004-03-01-0000.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter() :
    print(node.tag, node.attrib,node.text)
