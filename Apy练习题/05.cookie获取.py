import requests

# url = 'https://www.juzikong.com/u/df462d53-ed44-4028-8fac-3214d55a6d63'
url = 'https://api.juzikong.com/n0/auth/login'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# r = requests.get(url)
# print(r.cookies)
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
print(response.text)
