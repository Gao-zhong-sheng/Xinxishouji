# 创建一个test。txt文件

# open(文件的路径,模式)
# 模式: w 可写
#      r  可读
# 打开文件
# fp = open('test.txt'.'w')
# fp.write('hello world')

# 文件夹是不是可以创建
fp = open('demo.txt', 'w')

# 文件的关闭
fp.close()
