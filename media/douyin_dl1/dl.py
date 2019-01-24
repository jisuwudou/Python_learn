# -*- coding:utf-8 -*-
from splinter.driver.webdriver.chrome import Options, Chrome
from splinter.browser import Browser
from contextlib import closing
import requests, json, time, re, os, sys


class douyin():
    def __init__(self):
        pass

    """
    视频下载
    Parameters:
        video_url: 带水印的视频地址
        video_name: 视频名
    Returns:
        无
    """

    def video_downloader(self, video_url, video_name=r'douyinsss.mp4'):

        size = 0
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
        try:
            with closing(requests.get(video_url, headers=headers, stream=True, verify=False)) as response:
                chunk_size = 1024
                # print(response.text)
                content_size = int(response.headers['content-length'])
                if response.status_code == 200:
                    sys.stdout.write('  [文件大小]:%0.2f MB\n' % (content_size / chunk_size / 1024))
                    """
                    with open(video_name, 'ab') as file:
                        file.write(response.content)
                        file.flush()
                        print('receive data，file size : %d   total size:%d' % (os.path.getsize(video_name), content_size))
                    """
                    with open(video_name, "wb") as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                            size += len(data)
                            file.flush()

                            # sys.stdout.write('  [下载进度]:%.2f%%' % float(size / content_size * 100) + '\r')
                            # sys.stdout.flush()
                    print('视频下载完了...')
        except Exception as e:
            print(e)
            print('下载出错啦.....')

    """
    视频下载地址获取
    Parameters:
        video_url: 带水印的视频地址
    Returns:
        视频下载链接，视频名字
    """

    def downloadUrlGet(self, video_url):
        name = ''
        downloadUrl = ''
        headers = {
            'Proxy-Connection': 'keep-alive',
            'Host': 'v.douyin.com',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        req = requests.get(url=video_url, headers=headers, verify=False)
        newUrl = req.url

        # print(req.text)
        print('newUrl:%s' % newUrl)
        print(req.history)
        # 302重定向后的请求
        headers = {
            'Proxy-Connection': 'keep-alive',
            'Host': 'www.iesdouyin.com',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        req = requests.get(url=newUrl, headers=headers, verify=False)
        reply = req.text
        # print(reply)
        p = reply.find('playAddr: "') + len('playAddr: "')
        downloadUrl = reply[p: reply.find('"', p)]
        print('downloadUrl:%s' % downloadUrl)
        p = reply.find('"name nowrap">') + len('"name nowrap">')
        name = reply[p: reply.find('<', p)]
        print(name)
        return downloadUrl, name


"""  开始主任务  """
url = 'http://v.douyin.com/dU2Dsn/'
handel = douyin()
downloadUrl, name = handel.downloadUrlGet(url)
handel.video_downloader(url, name)
