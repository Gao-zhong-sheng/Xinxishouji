import requests

url = 'https://www.baidu.com'
response = requests.get(url=url)
# 一个类型和六个属性
# Response类型
# print(type(response))

# 一字符串的形式来返回网页的源码
# print(response.text)
# 设置响应的编码格式
# response.encoding = 'utf-8'
# 返回一个url的地址
# print(response.url)
# 返回的是二进制的数据
# print(response.content)
# 返回相应的状态信息
# print(response.status_code)
# 获取响应头的信息
# print(response.headers)

