import urllib.request
import urllib.parse
import json

# 怎么处理post请求
# demo百度翻译
# 1.输入地址栏内的链接
# url = 'https://fanyi.baidu.com/#en/zh/girl'
post_url = 'https://fanyi.baidu.com/sug'
data_dict = {
    'kw':'boy'
}
data = urllib.parse.urlencode(data_dict).encode('utf-8')

request = urllib.request.Request(url=post_url,headers={},data=data)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
# with open('fanyi.html','w',encoding='utf-8')as fp:
#     fp.write(content)