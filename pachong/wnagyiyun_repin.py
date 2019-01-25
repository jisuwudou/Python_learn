#网易云 热评
# https://music.163.com/
# https://music.163.com/weapi/v1/resource/comments/R_SO_4_494862393?csrf_token=

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/3/28 8:46
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : NetCloud_spider3.py
'''
@Description:
网易云音乐评论爬虫，可以完整爬取整个评论
部分参考了@平胸小仙女的文章(地址:https://www.zhihu.com/question/36081767)
post加密部分也给出了，可以参考原帖：
作者：平胸小仙女
链接：https://www.zhihu.com/question/36081767/answer/140287795
来源：知乎
'''
from Cryptodome.Cipher import AES
import base64
import requests
import json
import codecs
import time
import random
# 头部信息
headers = {
    # 'Host':"music.163.com",
    # 'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding':"gzip, deflate",
    # 'Content-Type':"application/x-www-form-urlencoded",
    # 'Cookie':"_iuqxldmzr_=32; _ntes_nnid=bfdbd07aaac7c124fdc38503b965c4b8,1548386605103; _ntes_nuid=bfdbd07aaac7c124fdc38503b965c4b8; WM_NI=zdTOoBfXD%2Bxt%2FxxKVl52zicv51MilB5UkLJQhL7KCUm0pKDBQqFFBCNsPzcaaSyFAGX5X7s3zuHRtgbzfKhO%2BlJCQCiPdPpHlbVnvL9DLe%2Bb%2F0NtnTsMdFYTaJ48uoM2MjI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea8c44d96b3a2afd279adef8ea3d14f869e9abbee6da88aaea7dc6087b796d7f02af0fea7c3b92ababc9cb0ee4aa6888cccfb80eda8b8acd568f7eeb68ae27ef7ef838aef4af78ba5adc95bac94f9acc25faff0c0acc74a93af8aa7c1498eada09be26ba38db7a7c44d9ceb98d8f239baab88b3f76da2a6aaaceb45e9b486a4d449ab90acb1f344b0be9a8ff548fb9c8486aa6aedf08295ed60b193aca7dc60a396fcd9f8658fee838bcc37e2a3; WM_TID=NyHTsYpWIMVERAABUAI4hZEfFNSViZrn; JSESSIONID-WYYY=4v6vCnztl8%2FogQeGszJ7%2BdH%2BAX5JjYOp0%2BDpEpCe53bj5W3yN09MOyfy2r0tU26OSXu1XnDtuj6Bf77ocbNEtdGdahJbQPTDAAvZaCEJy%2FSFF7uRdrrwXI%5ClxGljXHOVgD2G3RzIo%2BS0S6CEdlEegvSZ5Ye373%2BkCsAKyNgayqQtrJvi%3A1548405367855",
    # 'Connection':"keep-alive",
    # 'Referer':'http://music.163.com/',

    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '474',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=bfdbd07aaac7c124fdc38503b965c4b8,1548386605103; _ntes_nuid=bfdbd07aaac7c124fdc38503b965c4b8; WM_NI=zdTOoBfXD%2Bxt%2FxxKVl52zicv51MilB5UkLJQhL7KCUm0pKDBQqFFBCNsPzcaaSyFAGX5X7s3zuHRtgbzfKhO%2BlJCQCiPdPpHlbVnvL9DLe%2Bb%2F0NtnTsMdFYTaJ48uoM2MjI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea8c44d96b3a2afd279adef8ea3d14f869e9abbee6da88aaea7dc6087b796d7f02af0fea7c3b92ababc9cb0ee4aa6888cccfb80eda8b8acd568f7eeb68ae27ef7ef838aef4af78ba5adc95bac94f9acc25faff0c0acc74a93af8aa7c1498eada09be26ba38db7a7c44d9ceb98d8f239baab88b3f76da2a6aaaceb45e9b486a4d449ab90acb1f344b0be9a8ff548fb9c8486aa6aedf08295ed60b193aca7dc60a396fcd9f8658fee838bcc37e2a3; WM_TID=NyHTsYpWIMVERAABUAI4hZEfFNSViZrn; JSESSIONID-WYYY=4v6vCnztl8%2FogQeGszJ7%2BdH%2BAX5JjYOp0%2BDpEpCe53bj5W3yN09MOyfy2r0tU26OSXu1XnDtuj6Bf77ocbNEtdGdahJbQPTDAAvZaCEJy%2FSFF7uRdrrwXI%5ClxGljXHOVgD2G3RzIo%2BS0S6CEdlEegvSZ5Ye373%2BkCsAKyNgayqQtrJvi%3A1548405367855',
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    'Referer': 'https://music.163.com/song?id=494862393',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# 设置代理服务器
proxies= {
            'http:': 'http://110.179.67.*:*',
            'http:': 'https://114.215.95.*:*',
            'http:': 'http://202.38.92.*:*',
            'http:': 'http://218.20.54.*:*',
            'http:': 'http://221.228.17.*:*',
        }
# 494862393
# offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
# first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}' # 第一个参数
second_param = "010001" # 第二个参数
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# 第四个参数
forth_param = "0CoJUm6Qyw8W8jud"

UA = ["UA_1", "UA_2"]




# 获取参数
def get_params(page): # page为传入页数
    iv = b"0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    if(page == 1): # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page-1)*20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' %(offset,'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(str(h_encText,'utf-8'), second_key, iv)
    return h_encText

# 获取 encSecKey
def get_encSecKey():
    encSecKey = "218593db29c6e104f337331d159c4e8acc36c34265c43f4a282e994647fad84a87ecd37cd29a9d2256dba666494366f966946a434aed29efb6a6fe395c2af211e2ce8d7214e301d3df7556ac26eafee3b1aeea7284c70dd313a14c136973e7639229e14af1990e7f9a436879d7937e52667ad2e9ec92fcbfb6d43d6daff0defc"
    return encSecKey


# 解密过程
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    key = key.encode('utf-8')
    # iv = iv.encode('utf-8')
    encryptor = AES.new(key, AES.MODE_CBC,iv)
    encrypt_text = encryptor.encrypt(text.encode('utf-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def _choose_randomly(l):
    random.shuffle(l)
    return l[0]

# 获得评论json数据
def get_json(url, params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    headers["User-Agent"] = _choose_randomly(UA)
    response = requests.post(url, headers=headers, data=data,proxies=proxies)
    return response.content

# 抓取热门评论，返回热评列表
def get_hot_comments(url):
    hot_comments_list = []
    hot_comments_list.append(u"用户ID 用户昵称 用户头像地址 评论时间 点赞总数 评论内容\n")
    params = get_params(1) # 第一页
    encSecKey = get_encSecKey()
    json_text = get_json(url,params,encSecKey)
    json_dict = json.loads(json_text)
    hot_comments = json_dict['hotComments'] # 热门评论
    print("共有%d条热门评论!" % len(hot_comments))
    for item in hot_comments:
            comment = item['content'] # 评论内容
            likedCount = item['likedCount'] # 点赞总数
            comment_time = item['time'] # 评论时间(时间戳)
            userID = item['user']['userID'] # 评论者id
            nickname = item['user']['nickname'] # 昵称
            avatarUrl = item['user']['avatarUrl'] # 头像地址
            comment_info = userID + " " + nickname + " " + avatarUrl + " " + comment_time + " " + likedCount + " " + comment + u"\n"
            hot_comments_list.append(comment_info)
    return hot_comments_list

# 抓取某一首歌的全部评论
def get_all_comments(url):
    all_comments_list = [] # 存放所有评论
    all_comments_list.append(u"用户ID 用户昵称 用户头像地址 评论时间 点赞总数 评论内容\n") # 头部信息
    params = get_params(1)
    encSecKey = get_encSecKey()
    json_text = get_json(url,params,encSecKey)
    json_dict = json.loads(json_text)
    comments_num = int(json_dict['total'])
    if(comments_num % 20 == 0):
        page = comments_num / 20
    else:
        page = int(comments_num / 20) + 1
    print("共有%d页评论!" % page)
    for i in range(page):  # 逐页抓取
        params = get_params(i+1)
        encSecKey = get_encSecKey()
        json_text = get_json(url,params,encSecKey)
        json_dict = json.loads(json_text)
        if i == 0:
            print("共有%d条评论!" % comments_num) # 全部评论总数
        for item in json_dict['comments']:
            comment = item['content'] # 评论内容
            likedCount = item['likedCount'] # 点赞总数
            comment_time = item['time'] # 评论时间(时间戳)
            userID = item['user']['userId'] # 评论者id
            nickname = item['user']['nickname'] # 昵称
            avatarUrl = item['user']['avatarUrl'] # 头像地址
            comment_info = unicode(userID) + u" " + nickname + u" " + avatarUrl + u" " + unicode(comment_time) + u" " + unicode(likedCount) + u" " + comment + u"\n"
            all_comments_list.append(comment_info)
        print("第%d页抓取完毕!" % (i+1))
    return all_comments_list


# 将评论写入文本文件
def save_to_file(list,filename):
        with codecs.open(filename,'a',encoding='utf-8') as f:
            f.writelines(list)
        print("写入文件成功!")

if __name__ == "__main__":
    start_time = time.time() # 开始时间
    songid = 494862393
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%d/?csrf_token=" % songid
    filename = u"eden.txt"
    all_comments_list = get_all_comments(url)
    save_to_file(all_comments_list,filename)
    end_time = time.time() #结束时间
    print("程序耗时%f秒." % (end_time - start_time))