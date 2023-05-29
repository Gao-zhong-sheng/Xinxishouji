import urllib.request
import urllib.parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
start_page = 1
end_page = 5
name= input("java")
for page in range(start_page, end_page + 1):
    url = f'https://tieba.baidu.com/f?kw={name}&ie=utf-8&pn={(page - 1) * 50}'
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    text = response.read().decode('utf-8')
    file_path = f'page{page}.html'
    with open(file_path,'w',encoding='utf-8')as fp:
        fp.write(text)
    print(file_path,"下载完成")
print("所有文件下载完成")