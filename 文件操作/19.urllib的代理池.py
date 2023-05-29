import urllib.request
import random

proxies = [
    {'http':'118.24.219.151:16817'},
    {'http':'118.24.219.151:16817'}
]
proxies = random.choice(proxies)
url = 'http://www.bai.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('daoli1.html','w',encoding='utf-8') as fp:
    fp.write(content)