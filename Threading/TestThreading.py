# https://www.cnblogs.com/owasp/p/6413480.html
#多线程下载一张图片
import threading
import requests
import time
import os
import sys

class DownloadThreading(threading.Thread):
    def __init__(self,url,startpos,endpos,f):
        super(DownloadThreading,self).__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f

    def download(self):
        print("start thread:%s at %s" % (self.getName(), time.time()))
        headers = {"Range": "bytes=%s-%s" % (self.startpos, self.endpos)}
        res = requests.get(self.url, headers=headers, verify=False)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        print("stop thread:%s at %s" % (self.getName(), time.time()))

    pass


# http://upload.cankaoxiaoxi.com/2016/0304/1457057742544.jpg
if __name__ == '__main__':#作为模块被导入时是逻辑否，自己作为主文件启动时逻辑true
    print('name = main')
    url = ''
    file_name = 'none url'
    if len(sys.argv) > 1:
        url = sys.argv[1]
        file_name = url.split('/')[-1]
    else:
        url = 'https://upload-images.jianshu.io/upload_images/14701230-149f55dcdffcebf3'
        file_name = url.split('/')[-1]

    req_heads = requests.head(url, verify=False)
    filesize = int(req_heads.headers['Content-Length'])
    print("%s filesize:%s" % (file_name, filesize))

    treadMax = 3
    threading.BoundedSemaphore(treadMax)

    per_step_size = filesize // treadMax
    print("per_step_size = " + str(per_step_size))

    # 请空并生成文件
    tempf = open(file_name, 'w')
    tempf.close()

    index = treadMax
    with open(file_name, 'rb+') as f:

        while index > 0:

            t = DownloadThreading(url, (index - 1) * per_step_size, index * per_step_size, f)
            t.download()
            index -= 1
        pass
