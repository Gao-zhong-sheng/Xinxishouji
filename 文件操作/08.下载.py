import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径 filename文件名字
# 在python中   可以变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')


# 下载图片
# url_img = 'https://i03piccdn.sogoucdn.com/52629fe36ba69967'
# urllib.request.urlretrieve(url=url_img,filename='lisa.jpg')


# 下载视频
url_vido = 'https://www.bilibili.com/5be95afb-7903-49a4-aad2-5e0177fe91d3'
urllib.request.urlretrieve(url_vido,'sw.mp4')