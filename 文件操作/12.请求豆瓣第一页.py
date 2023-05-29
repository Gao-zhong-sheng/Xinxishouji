import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 1请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 2获取相应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 3 数据下载到本地  open方法默认情况下使用的是gbk的编码 如果我们保存汉字中文 需要在open方法中 指定utf-8
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)






