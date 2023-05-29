# 使用urllib
import urllib.request

# 定义一个urllib 访问地址
url = 'https://www.baidu.com/'

# 2模拟浏览器向服务器发送请求  response相应

response = urllib.request.urlopen(url)

# 3 响应中的页面的源码
# read 方法返回二进制数据
# 将二进制编程字符串的过程叫做解码
content = response.read().decode('UTF-8')

# 打印数据
print(content)










