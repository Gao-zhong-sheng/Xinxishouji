# urlencode应用场景:多个参数的时候


# https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.parse
import urllib.request

# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
# a = urllib.parse.urlencode(data)
# print(a)
base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
new_data = urllib.parse.urlencode(data)
# 发送请求路径
url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

}
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
# 获取网页源码的数据
content = response.read().decode('utf-8')
# 打印
print(content)
