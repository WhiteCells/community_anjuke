from lxml import etree


html_path = './demo.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# print(html_content)

root = etree.HTML(html_content)

value = root.xpath('//form//input[@type="submit"]/@value')

print(value[0])