import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 将周杰伦三个字编程unicode的格式
# 我们需要依赖于urllib.parse
# name = urllib.parse.quote('周杰伦')
# print(name)
# https://www.bilibili.com/video/av502262544/?fromvsogou=1&bsource=sogou&fr=seo.bilibili.com&vd_source=3db51f9bf867db895f11c26fada41ab0

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

print(content)
