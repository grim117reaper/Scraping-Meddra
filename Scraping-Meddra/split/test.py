import xml.etree.ElementTree

i = 0
tree = xml.etree.ElementTree.parse('combined.xml')
root = tree.getroot()
for level0 in root:
    i = i +1
    print(level0.attrib)
    for level1 in level0:
        i = i +1
        print(level1.attrib)
        for level2 in level1:
            i = i +1
            print(level2.attrib)
            for level3 in level2:
                i = i +1
                print(level3.text)

print(i)
