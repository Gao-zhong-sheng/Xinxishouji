from lxml import etree

# xpath 解析
# （1）本地文件                                           etree.parse
# （2）服务器的响应的数据 response.read().decode('utf-8')   etree.HTML()
# xpath 解析本地文件
tree = etree.parse('21.xpath的基本使用.html')

# tree.xpath('xpath路径')

# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')
# 查找所有id的属性li标签  谓词查询
li_list = tree.xpath('//ul/li[@id]/text()')

print(li_list)
print(len(li_list))