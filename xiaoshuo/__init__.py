import requests
from bs4 import BeautifulSoup
import os

#下载总排行 https://www.80txt.com/sort/1.html 总推荐榜 https://www.80txt.com/top/allvisit/1.html

# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
'Accept-Encoding':"gzip, deflate, sdch, br",
'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3176.400 QQBrowser/9.6.11576.400"}
all_url = 'https://www.80txt.com/top/allvisit/1.html' #'http://www.mzitu.com/all'  ##开始的URL地址

requests.packages.urllib3.disable_warnings()#不加这句，https请求有问题 https://blog.bbzhh.com/index.php/archives/111.html
start_html = requests.get(all_url,  headers=headers, verify=False)  ## verify=False   使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
# print(start_html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
# print('hello w')

def savefile(lastDownUrl):
    filename = os.path.basename(lastDownUrl)
    # filename = filename[]
    filename = filename[0:len(filename) - 4]

    # print(os.path)
    # filtPath = "F:\\books\\"+filename
    filtPath = "F:\\books_1-9\\"
    if not os.path.exists(filtPath):
        os.makedirs(filtPath)

    print(os.path.exists(filtPath+filename))
    if os.path.exists(filtPath+filename):
        print("已经下载了跳过："+filename)
        return
    os.chdir(filtPath)
    bookres = requests.get(lastDownUrl,headers=headers,verify=False)
    size = len(bookres.content)
    # print(size)
    # print(bookres)
    f = open(filename+'.zip','wb')
    f.write(bookres.content)
    f.close()
    print("成功保存：filename=%s size=",filename,size)
    return

souphandle = BeautifulSoup(start_html.text,'lxml')
soupList = souphandle.find_all(class_='book_bg')

total = len(soupList)
for i in range(len(soupList)):
    print("处理第：%d/%d",i,total)
    # totalindex+=1
    item = soupList[i]

    item_url = item.find('a')['href']
    print(item_url)
    item_html = requests.get(item_url,headers=headers,verify=False)
    # print(item_html.text)
    itemSoup = BeautifulSoup(item_html.text,'lxml')
    itemSecList = itemSoup.find(class_='soft_info_r').find_all('a')
    for item2 in itemSecList:

        if not item2.has_attr('class'):
            downloadhtml = item2['href']
            if downloadhtml[-9:-1] == "down.htm":
                downloadhtml = 'https://www.80txt.com/'+downloadhtml
                # print(downloadhtml)
                downloadhtml = requests.get(downloadhtml, headers=headers, verify=False)
                print("编码="+downloadhtml.encoding)
                downloadhtml.encoding = 'utf-8'
                souphandle3 = BeautifulSoup(downloadhtml.text, 'lxml')
                soupList3 = souphandle3.find_all(class_='pan_url')

                for index in range(len(soupList3)):
                    if index == 1:
                        lastDownUrl = soupList3[index].find('a')['href']
                        print(lastDownUrl)
                        savefile(lastDownUrl)
    # break



