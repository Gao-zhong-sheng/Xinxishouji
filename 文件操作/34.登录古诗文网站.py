import requests

url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 获取网页的源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码 然后获取__VIEWSTATE    __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')
# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
# __VIEWSTATEGENERATOR
viewstategenertor = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
# import urllib.request
session = requests.session()
# 获取url的内容

response_code = session.get(code_url)
# 注意此时要是用二进制数据 因为我们使用的是图片的下载
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# 获取了验证码的图片之后 下载到本地 然后观察验证码 观察之后 然后再控制台输入验证码输入这个
# 就可以将这个值给code的参数 就可以登陆
code_name = input('请输入你的验证码')

# 点击登陆
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenertor,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '3105766277@qq.com',
    'pwd': '811020.10.20',
    'code': code_name,
    'denglu': '登录'
}
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
