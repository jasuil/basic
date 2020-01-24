from xml.etree.ElementTree import parse, SubElement, dump, Element

node = Element("note2")
to = Element("to2")
book = Element("book")

to.text = "you"
book.text = "python"

node.append(to)
node.append(book)
node.insert(0, book)

SubElement(node, "address").text = "sss"

dump(node)




# tree = parse("myXml.xml")
# root = tree.getroot();
#
# print(root.get("date"))
# print(root.get("head", "default"))
# print(root.keys())
# print(root)
#
# node_from = root.find("from")
# node_from2 = root.findall("from")
# node_from3 = root.findtext("from")
#
# print(node_from)
# print(node_from2)
# print(node_from3)