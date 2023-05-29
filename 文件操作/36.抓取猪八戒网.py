import requests
from lxml import etree
url = "https://zhengzhou.zbj.com/sem/index?pmcode=137535808&utm_source=bdpz&utm_medium=SEM"
response = requests.get(url)
# print(response.text)
html = etree.HTML(text=response.text)
# 拿到每一个服务商的div /html/body/div[1]/div[5]/div[4]/div/div/div/div[1]
divs = html.xpath('/html/body/div[1]/div[5]/div[4]/div/div/div/div')

for div in divs:
    price = div.xpath('./div/div/a/div[2]/div[1]/span[1]/text()')
    print(div)