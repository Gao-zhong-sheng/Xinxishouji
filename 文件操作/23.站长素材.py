import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
    else:
        url = f'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    # 在没有加载出来的时候src2 加载出来是src 但是！要按src2算
    src_list = tree.xpath('//div[@class="container"]//img/@src')
    for i in range(len(name_list)):
        # print(src_list)
        src = src_list[i]
        # print(src)
        name = name_list[i]
        print(name,src)
        url = 'https:' + src
        # print(name, url)
        urllib.request.urlretrieve(url=url, filename=name + '.jpg')


# https: // scpic1.chinaz.net / files / default / imgs / 2022 - 11 - 04 / 259028759
# b1b18fe_s.jpg
# https:../ static / common / com_images / img - loding.png
if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        # （1）请求对象的定制
        # print(page)
        request = create_request(page)

        #  (2)获取网页的源码
        content = get_content(request)
        # print(content)

        # (3)
        down_load(content)
