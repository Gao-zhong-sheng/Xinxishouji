# 使用urllib
import urllib.request

# 定义一个urllib 访问地址
url = 'https://www.baidu.com/'

# 2模拟浏览器向服务器发送请求  response相应
# response是HTTPResponse类型
# print(type(response))

response = urllib.request.urlopen(url)

# 3 响应中的页面的源码
# read 方法返回二进制数据
# 将二进制编程字符串的过程叫做解码  read(5)表示反回多少个字节
# content = response.read().decode('UTF-8')

# 读取一行

# content = response.readline()

# 读取全部的数据 但是后面.decode()不能使用

content = response.readlines()

# 返回状态码 如果是200了 那么就证明我们的逻辑没有错
# print(response.getcode())
#
# # 返回url的地址
# print(response.geturl())
#
# # 获取状态信息
# print(response.getheaders())

# 打印数据
print(content)










