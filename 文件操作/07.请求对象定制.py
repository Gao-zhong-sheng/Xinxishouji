import urllib.request

url = 'https://www.baidu.com'

# url的组成
# http/https         www.baidu.com     80/443       s       wd=周杰伦
#  协议                主机              端口号        路径    参数      锚点
# http      80
# http      443
# mysql     3306
# oracle    1521
# redis     6379
# mongodb   27017

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
