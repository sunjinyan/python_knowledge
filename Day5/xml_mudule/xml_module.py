xml = '''

'''
import xml.etree.ElementTree as ET

tree =  ET.parse("test.xml")
root = tree.getroot()

print(root.tag)

for child in root:
    print(child.tag,child.attrib)
    for i in  child:
        print(i.tag,i.text)

# 只便利单个节点
for node in root.iter('year'):
    print(node.tag,node.text)
    node.text = str("1111")
    node.set('update_by',"Alex")

tree.write('out.xml')

# 删除
for node in root.findall('country'):
    rank = int(node.find('rank').text)
    if rank > 50:
        root.remove(node)

tree.write('output.xml')


# 自己创建xml文档：
new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
ages = ET.SubElement(name2, "age")
ages.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

