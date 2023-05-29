import requests
from lxml import etree

url = 'http://www.ibiqu.org/book/38857/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
r = requests.get(url=url)
r.encoding = 'gbk'
content =r.text
# print(content)
a_xpath = '//div[@id="list"]//dl//dd/a'
root = etree.HTML(content)

print(root)
a_list = root.xpath(a_xpath)

# print(a_list)
# for a_node in a_list:
#     title = a_node.xpath('./text()')[0]
    # href = a_node.xpath()
    # print(title)
