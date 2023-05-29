import urllib.request
from lxml import etree


# https://sc.chinaz.com/tupian/
# https://sc.chinaz.com/tupian/index_2.html   变的是页码，但是第一页没有加这个（结构不一样

def get_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/meinvxiezhen.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meinvxiezhen_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def get_download(content):
    # 定制tree对象
    tree = etree.HTML(content)
    # 使用xpath获取图片名字和源码
    alt_list = tree.xpath('//div[@class="item masonry-brick"]/img/@alt')
    src_list = tree.xpath('//div[@class="item masonry-brick"]/img/@src2')
    for i in range(0, len(alt_list)):
        url = 'https:' + src_list[i]
        name = alt_list[i]
        print(url,name)
        # urllib.request.urlretrieve(url=url, filename=name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入要下载的起始网页：'))
    end_page = int(input('请输入要下载的结束网页：'))
    for i in range(start_page, end_page + 1):
        # 定制对象
        request = get_request(i)
        # 获取content内容
        content = get_content(request)
        # 下载文件
        get_download(content)
