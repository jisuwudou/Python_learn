#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys
import json
import time

import re
import urllib3
urllib3.disable_warnings( )
# reload(sys)
# sys.setdefaultencoding('utf8')
headers = {
        'Accept': 'application/json, text/plain, */*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Content-Length': '44',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_T_WM=0f1f2c8e92c72e7d986dc63fefb87f64; WEIBOCN_FROM=1110005030; SUB=_2A25xSsWIDeRhGeNP7lQU9inFyz6IHXVStOvArDV6PUJbkdAKLRnnkW1NTm4vJQhBOMoBnTYmc_Xsb0Q5Kt7zj_FC; SUHB=010WrrCurcsPXG; SCF=AolRZuJB_m_0q_bt_OvesfL4DHtN83fNn0fjNIwq6AeJBIX8Clm38_hUKhBRBHAnlniEHictjc3nUy1Wkz17WPw.; SSOLoginState=1548662232; MLOGIN=1; XSRF-TOKEN=089811; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174',
        'Host': 'm.weibo.cn',
        # 'MWeibo-Pwa': '1',
        # 'Origin': 'https://m.weibo.cn',
        # 'Referer': 'https://m.weibo.cn/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest'

        # 'RA-Ver': '3.0.8',
        # 'Cache-Control': 'max-age=0',
        # 'RA-Sid': 'B781E81A-20150402-024118-ce25e1-ba5345',
    }
headetr2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': '_T_WM=02481a12ce37d9d4f21b04b904751066; WEIBOCN_FROM=1110005030; ALF=1550737541; SCF=ApGZ4bfK3adwIoAzlGTh8eRsymmH4pTWZPe3-Nmx_Dw9jgnD0midsGuwegVkUDlB1jm5oMeAhX1KoWD9xVocV-4.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFSIx.J365qPnyElZHmG8YT5JpX5K-hUgL.Fo-pSKqfSoM4ehz2dJLoIXjLxKnLBo-LBoMLxKBLBonLB-2LxK.L1-eLBonLxKqLBo5L1KBLxKML1hzLBo.LxKML1-2L1hBLxK-L1K5L12BLxK-LB-BL1KM_PEXt; SUB=_2A25xQq2iDeRhGeNP7lQU9inFyz6IHXVSzDPqrDV6PUJbkdAKLUzwkW1NTm4vJWoxgp-wad8_nTSLp4MkOlN_HgFs; SUHB=0LcCj9isveaf5y; SSOLoginState=1548148210; MLOGIN=1; XSRF-TOKEN=489af6; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803',
        'Cookie': '_T_WM=d8294973580ab8188d79cef5d9c8db3f; SUB=_2A25xVH1HDeRhGeNP7lQU9inFyz6IHXVStwMPrDV6PUJbkdAKLROmkW1NTm4vJUPd-Qa0groU8jv2uBALQMxl5TCJ; SUHB=0M2V2GYNyGsLM6; SCF=AjwZ6V68VXmZ7JLptkr_oAL12cn4AHsPVEw-UAb9zlQaEbFU1gY0s8MVHCfes7aedRsv3GLnXWiSk7iu_iIatw4.; SSOLoginState=1548750103; MLOGIN=1; XSRF-TOKEN=e45f1e; WEIBOCN_FROM=1110005030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076036584157870%26fid%3D1076036502644922%26uicode%3D10000011',
        'Host': 'm.weibo.cn',
        'RA-Sid': 'B781E81A-20150402-024118-ce25e1-ba5345',
        'RA-Ver': '3.0.8',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36',
        'Referer': 'https://m.weibo.cn/message',
    }

# groupchatstheaders = {
#
# }
def guanzhugroup(groupid):

    for nums in range(11, 49):  # 这里是模拟页数
        print('***************第几页='+str(nums))
        # urluser = "https://m.weibo.cn/groupChat/userChat/groupMembersList?group_id=4197189808619503&page="+str(nums)
        urluser = "https://m.weibo.cn/groupChat/userChat/groupMembersList?group_id=%s&page=%d" % (groupid, nums)

        respone = requests.get(urluser, headers=headetr2, verify=False)

        # print(respone)
        print(respone.text)
        pattern = re.compile('\['+'(.*?)'+']',re.S)
        json1 = pattern.findall(respone.text)[0]+']}'

        json_base = json.loads(json1)
        print(json_base)

        card_group = json_base['card_group']

        st_url = 'https://m.weibo.cn/api/config/'
        st_respone = requests.post(st_url, headers=headetr2, verify=False)
        st_json = json.loads(st_respone.content)
        print('st = ' + st_json['data']['st'])

        # print(len(card_group))
        for num in range(0, len(card_group)):
            member = card_group[num]
            print(member['member']['id'])
            print(print(member['member']['screen_name']))



            postData2 = {"uid": member['member']['id'], 'st': st_json['data']['st']}  # post请求传的数据
            url = 'https://m.weibo.cn/api/friendships/create'

            # https: // m.weibo.cn / api / friendships / create
            respone1 = requests.post(url, data=postData2, headers=headetr2,verify=False)
            print(respone1.text)
            json_str = respone1.content

            # print(json_str.decode('gbk').encode('utf-8').decode('unicode_escape'))


            chatgroup_url = 'https://m.weibo.cn/groupChat/userChat/chat?group_id=' + str(groupid)
            chatgroup_respone = requests.get(chatgroup_url, headers=headetr2, verify=False)
            print(chatgroup_respone.text)
            pattern = re.compile(r'"st":"(.)"')
            chat_st = re.findall(pattern, chatgroup_respone.text)
            # test = chatgroup_respone.text.find('st":')
            # print(test)
            sendmsg_url = 'https://m.weibo.cn/groupChat/userChat/sendMsg'
            sendmsg_data = {
                'content': '@%s 关注了回粉' % member['member']['screen_name'],
                'st': st_json['data']['st'],
                'group_id': groupid,
            }
            sendmsg_respone = requests.post(st_url, headers=headetr2, data=sendmsg_data, verify=False)
            print('send msg ret = '+sendmsg_respone.text)

            time.sleep(10)


        # content: 回粉啊
        # group_id: 4075182799395477
        # st: a26cd1

    time.sleep(30)

guanzhugroup(4075182799395477)

# dianzanFirendsurl = "https://m.weibo.cn/feed/friends?max_id="#获取关注的用户发的微博
# giveHeartUrl = 'https://m.weibo.cn/api/attitudes/create'#点赞
# dianzanshu=1
# def dianzan(max_id):
#
#     while max_id != "" and max_id != None and max_id != 0 and max_id != '0':
#
#         needStop = False
#         urluser = dianzanFirendsurl + str(max_id)
#         respone = requests.get(urluser, headers=headers, verify=False)
#         print(respone.text)
#         jsondata = json.loads(respone.content)['data']
#         max_id = jsondata['max_id']
#         userdatas = jsondata['statuses']
#
#         print('max id =' + str(max_id))
#         for index in range(0,len(userdatas)):
#             # print(type(userdatas[index]['id']))
#             giveHeartData = {
#
#                 "id": userdatas[index]['id'],
#                 "attitude": "heart",
#                 "st": "78d37a",
#             }
#
#             heartResponse = requests.post(giveHeartUrl, data=giveHeartData, headers=headers, verify=False)
#             heartJson = json.loads(heartResponse.content)
#             print('name = '+userdatas[index]['user']['screen_name']+' id = '+str(userdatas[index]['id']))
#             if heartJson['ok'] == 0:
#                 print("******点赞失败="+heartJson['errno']+" msg="+heartJson['msg'])
#                 needStop = True
#                 break
#             # print(heartResponse.text)
#             print("总点赞数="+str(dianzanshu))
#             dianzanshu += 1
#
#             time.sleep(2)
#
#         if needStop:
#             break


    # print(jsaondata)
    # pattern = re.compile('\[' + '(.*?)' + ']', re.S)


# dianzan(4333465032334598)
    # https://m.weibo.cn/groupChat/userChat/groupMembers?group_id=4197189808619503