# fp = open('test.txt', 'r')
#
# fp.read()
#
# fp.close()
try:
    # 可能出现异常
    fp = open('test.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('文件丢失创建文件后重试')