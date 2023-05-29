import urllib.request
import urllib.parse


def create_request(page):
    url = 'https://movie.douban.com/j/chart/top_list?type=7&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(resquest):
    response = urllib.request.urlopen(resquest)
    content = response.read().decode('utf-8')

    return content


def down_load(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))
    for page in range(start_page, end_page + 1):
        # 每一页都有自己的请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page, content)
