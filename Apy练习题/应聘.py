education = int(input('学历是否专科以上，是为1，否为0:'))
major = int(input('专业是否为会计，是为1，否为0:'))
work = int(input('有两年的工作经验，是为1，否为0:'))
""" 
    if语句判断的条件是整数类型 1 如果传入字符串 就会报错
    除了整数类型 其他类型都会报错 传入的参数可以为1 其他整数类型也可以
    比如-1, 3, 5 都是可以的在这个程序中 苏同学懂了没 ￣へ￣
"""
if education == 1:
    print('学历满足要求')
    if major == 1:
        print('专业不对口')
        if work == 1:
            print('经验充足')
            print('恭喜，请参加面试')
        else:
            print('经验不足')
    else:
        print('专业不对口')
else:
    print('学历不够')
