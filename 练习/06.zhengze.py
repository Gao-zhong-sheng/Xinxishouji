from bs4 import BeautifulSoup
import requests

url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
content = response.text
soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenertor = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
code_name = input('请输入你的验证码')
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenertor,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '3105766277@qq.com',
    'pwd': '811020.10.20',
    'code': code_name,
    'denglu': '登录'}
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
