import urllib.request

url = 'https://weibo.com/ajax/statuses/config'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',

    'cookie': 'XSRF-TOKEN=_0PFbmYMpZDDr6RXyQ0lxhJT; SUB=_2A25O_RRaDeRhGeFJ41sX8yvOyDyIHXVtiwKSrDV8PUNbmtANLVKikW9NfskO7Ye3jKhgiPLOE3S5R9Pafl7N15zV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhE-jdFThhNXW5S3AGSqAip5JpX5KzhUgL.FoMN1h.ce0-Ee052dJLoIE2LxK.LB-zL1KnLxKBLBonLB-BLxKML1KBL1-qp1Kn4eh2t; ALF=1708824457; SSOLoginState=1677288458; _s_tentry=weibo.com; Apache=5099579889865.699.1677288550258; SINAGLOBAL=5099579889865.699.1677288550258; ULV=1677288550336:1:1:1:5099579889865.699.1677288550258:; WBPSESS=itv9JLRJGL_8jx8Djy3d8bk2N4uoTVxdsQ3LlvMMOZ7ftz4CSoKGKuyhj58GWz6z8esM11TPBPMbbAhjYCCDYAJor1NEtrdfdxVRF220WgqNURbB0iWegTwezuYoBCyer0mr_BpkSoaOrTrrj8ANMA==',
    'referer': 'https://weibo.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 请求对象的定制
# 登录的页面不是utf-8所以报错
# 请求头的的信息不够 所以访问不成功
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')
# 将数据保存到本地
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
