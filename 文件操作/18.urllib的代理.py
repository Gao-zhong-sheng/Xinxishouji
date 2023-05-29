import urllib.request

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问浏览器
#response = urllib.request.urlopen(request)

proxies = {
    'http':'222.74.73.202:42055'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')
# 保存数据
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
