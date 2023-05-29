import requests

url = 'https://www.baidu.com/s'
response = requests.get(url=url)
page = response.text
print(page)