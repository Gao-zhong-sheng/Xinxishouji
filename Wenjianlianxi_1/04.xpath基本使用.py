import urllib.request
import urllib.parse


url = "https://sc.chinaz.com/tupian/xingganmeinvtupian.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open("homepage.html",'w',encoding='utf-8')as fp:
    fp.write(content)
# 下载多媒体时一般采用的二进制方式存储
# json html 才会使用文本格式来存储
# 默认read 除开的数据就是b以此处字节类型 所不要再解码操作
# with open('test.jpg','wb')as fp:
#     fp.write(content)
# 首页加载了所有图片的链接 但是没有直接对所有图片的完成下载