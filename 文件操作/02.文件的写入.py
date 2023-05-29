# 写入数据
# # write方法
# fp = open('test', 'w')            # a追加
#
# fp.write('hello world, i am here\n' * 5)
#
# fp.close()
# 读取数据
fp = open('test','r')
# 默认情况下 read是一字节一字节的读效率比较低
# content= fp.read()
# print(content)

# readline是一行一行的读取  但是只能读取一行
# content = fp.readline()
# print(content)

# readlines可以按照行来读 但是会将所有的数据全部读取以列表形式返回
content = fp.readlines()
print(content)