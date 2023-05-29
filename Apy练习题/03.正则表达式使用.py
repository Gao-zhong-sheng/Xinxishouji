import re

# s = 'itheima1 @@python2 !!666 # itcast3'
# # match 从头开始匹配
# result = re.match('python', s)
# print(result)
# # search 搜索匹配
# result = re.search('python',s)
# print(result)
# result = re.findall('python',s)
# print(result)
# \W 匹配非单词字符
# \d 匹配数字，即0-9
# # result = re.findall(r'[a-zA-z0-9]',s)
# # print(result)
# # 匹配账号，只能有字母和数字组成 长度限制6-10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = '1234567abc'
# print(re.findall(r, s))
# 匹配qq号 要求纯数字 长度5-11 第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '112345678'
print(re.findall(r, s))
