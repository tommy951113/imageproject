from lxml import etree
xml = etree.parse('test.xml')
result = xml.xpath('./text()[1]')
print(result)