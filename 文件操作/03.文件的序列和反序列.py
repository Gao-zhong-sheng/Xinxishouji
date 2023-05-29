# import json
# #
# # fp = open('test.txt', 'w')
# # # 定义一个列表
# # name_list = ['zs', 'ls']
# #
# # # 导入json模块到该文件中
# #
# # # 序列化
# # # 将python对象编程json字符串
# # # 我们在使用scrapy框架的是时候 该框架会返回一个对象 我们将对象写入文件中就要使用json.dumps
# # names = json.dumps(name_list)
# # # 将name写入文件中
# # fp.write(names)
#
# # fp.close()
# # dump
# # 在将对象转换为字符串的同时，指定一个文件的对象 然后把转换后的字符串写入到这个文件里
# fp = open('test.txt','w')
#
# name_list = ['zs','ls']
# json.dump(name_list,fp)
# fp.close()
# # 反序列化
# # 将json的字符串变成一个python对象
# fp = open('test.txt','r')
# content = json.load(fp)
# print(content)
# # dumps 需要一个变量接收而 dump不需要接收
# # loads 需要一个变量接受   load不需要变量接受
#
#












