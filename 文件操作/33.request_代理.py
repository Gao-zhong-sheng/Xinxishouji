import requests
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
data = {
    'kw': 'ip'
}
response = requests.get(url=url, data=data, headers=headers)
content =response.text
with open('daili4.html','w',encoding='utf-8')as fp:
    fp.write(content)