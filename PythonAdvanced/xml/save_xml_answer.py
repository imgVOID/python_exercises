# Выполните сериализацию словаря контактов в формат XML.
# Ожидаемая структура xml-файла:
# <records><record num='1'><name></name><number></number></record></records>

from xml.etree import ElementTree as ET

data = {
           'names': ['Anna', 'Peter', 'Julia', 'Ivan'],
           'numbers': ['+380639439898', '+380539134868',
                       '+380939173261', '+380739234463'],
       }

root = ET.Element('records')
for index in range(len(data['names'])):
    record = ET.SubElement(root, 'record')
    record.attrib = {'num': str(index+1)}
    name = ET.SubElement(record, 'name')
    number = ET.SubElement(record, 'number')
    name.text = data['names'][index]
    number.text = data['numbers'][index]

tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8')
