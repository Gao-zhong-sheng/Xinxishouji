import json
import jsonpath

obj = json.load(open('store.json', 'r', encoding='utf-8'))
# 书店所有的作者
# author = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author)
# 所有的作者
# author = jsonpath.jsonpath(obj,'$..author')
# print(author)
# store下面的所有的元素
# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# store里面所有东西的price
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj,'$..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(book)

# 前面的两本书
# book_list = jsonpath.jsonpath(obj,'$..book[0,1]')
# book_list = jsonpath.jsonpath(obj,'$..book[:2]')
# print(book_list)

# 条件过滤需要在（）的前面加一个？
# 过滤出所有的包含isbn的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 那本书超过了10块钱
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
# print(book_list)