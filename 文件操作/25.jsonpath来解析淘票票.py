import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1677553880930_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=f16cd682881222dbb9367e19b3518910; cookie2=152a4dd680ba495a3901a6aa363a4483; v=0; _tb_token_=fdea8889336e; cna=qVaEHIk3cUMCAQHGEg499llO; x5secdata=xb65b750a572f965cf8e570de8491042951677551788a-717315356a1993109894abazc2caa__bx__fourier.taobao.com%3A443%2Frp; xlly_s=1; isg=BFFRjpAM1p23XjqJyzy_W5QfYF3rvsUwI0ok4TPmLZgt2nAsegtTAaczfK48Ul1o; tfstk=cXicBms6eqzX9S-tNjZXxeACOZtdaFY4Gcor4LtPYCkUSUiz3sxCzw5OTLVvOI71.; l=fBEE2EtuTqwESC6_BOfwFurza77OLIRfguPzaNbMi9fP_vCBRapAW68CFqT6CnGVEsAXJ3ub1k7yBPTr8y4F0xv9-ewh384LldTHBMpwL',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]
with open('解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
obj = json.load(open('解析淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)

