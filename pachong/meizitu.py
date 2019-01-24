import requests
from bs4 import BeautifulSoup
import os
# http://www.mmjpg.com/tag/boluoshe   http://www.mmjpg.com/tag/boluoshe/2 http://www.mmjpg.com/hot/
# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {
'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Host: www.mmjpg.com
# Referer: http://www.mmjpg.com/tag/miitao/6
# Upgrade-Insecure-Requests: 1
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
all_url = 'http://www.mmjpg.com/hot/' #'http://www.mzitu.com/all'  ##开始的URL地址

# def savefile(name):
#     path = "g:/pachong"
#     if not os.path.exists("g:/pachong"):
#         os.makedirs(path)   
def getSoupByUrl(url):
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    list = BeautifulSoup(html.text)
    return list

# start_html = requests.get(all_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
# print(start_html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)

# start_html.encoding='utf-8'
list = getSoupByUrl(all_url)
list = list.find_all('ul')
for index in range(len(list)):
    item = list[index]
    list2 = item.find_all('a')
    for index2 in range(len(list2)):
        url = list2[index2]['href']
        # print(url)
        # print(url[24:])
        secondlist = getSoupByUrl(url).find_all('a')

        path = "g:/pachong/"+url[24:]
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
        print("path = "+path)
        for index3 in range(10):
            index3 = index3 + 1
            imgurl = url+"/"+str(index3)+".jpg"
            print(imgurl)
            imgrespon = requests.get(imgurl,headers=headers)
            # print(str(index3))

        for item3 in secondlist:
            print(item3)
            # fullname = str(index3) + ".jpg"
            # f = open(fullname, 'ab')
            # f.write(imgrespon.content)
            # f.close()

    break