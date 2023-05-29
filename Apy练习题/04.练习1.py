import requests

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
data = {
    'kw': 'soon'
}
response = requests.post(url=url, headers=headers, data=data)
obj = response.json()
print(obj)
