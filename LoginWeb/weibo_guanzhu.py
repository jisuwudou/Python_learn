#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys
import json
import time

import re
# reload(sys)
# sys.setdefaultencoding('utf8')
def guanzhugroup(groupid):
    headetr2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': '_T_WM=02481a12ce37d9d4f21b04b904751066; WEIBOCN_FROM=1110005030; ALF=1550737541; SCF=ApGZ4bfK3adwIoAzlGTh8eRsymmH4pTWZPe3-Nmx_Dw9jgnD0midsGuwegVkUDlB1jm5oMeAhX1KoWD9xVocV-4.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFSIx.J365qPnyElZHmG8YT5JpX5K-hUgL.Fo-pSKqfSoM4ehz2dJLoIXjLxKnLBo-LBoMLxKBLBonLB-2LxK.L1-eLBonLxKqLBo5L1KBLxKML1hzLBo.LxKML1-2L1hBLxK-L1K5L12BLxK-LB-BL1KM_PEXt; SUB=_2A25xQq2iDeRhGeNP7lQU9inFyz6IHXVSzDPqrDV6PUJbkdAKLUzwkW1NTm4vJWoxgp-wad8_nTSLp4MkOlN_HgFs; SUHB=0LcCj9isveaf5y; SSOLoginState=1548148210; MLOGIN=1; XSRF-TOKEN=489af6; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803',
        'Cookie': '_T_WM=af39a638502e4ba3ee3b599beb6f2923; SUB=_2A25xShWuDeRhGeNP7lQU9inFyz6IHXVStLvmrDV6PUJbkdAKLW7YkW1NTm4vJWGfL4w49b02YGA6tHo3gcuykaC6; SUHB=0h1ZaUW1W0SArJ; SCF=AolRZuJB_m_0q_bt_OvesfL4DHtN83fNn0fjNIwq6AeJ1p6zIFRgtL6D0MGYiihc_rVjAilR7H_Z6M5bJdqL7MI.; SSOLoginState=1548641790; MLOGIN=1; XSRF-TOKEN=6e7e13; WEIBOCN_FROM=1110005030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076036475520716%26fid%3D1076036836936249%26uicode%3D10000011',
        'Host': 'm.weibo.cn',
        'RA-Sid': 'B781E81A-20150402-024118-ce25e1-ba5345',
        'RA-Ver': '3.0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36'
    }
    for nums in range(33, 41):  # 这里是模拟页数
        print('第几页='+str(nums))
        urluser = "https://m.weibo.cn/groupChat/userChat/groupMembersList?group_id=4197189808619503&page="+str(nums)
        respone = requests.get(urluser, headers=headetr2, verify=False)

        print(respone)
        print(respone.text)
        pattern = re.compile('\['+'(.*?)'+']',re.S)
        json1 = pattern.findall(respone.text)[0]+']}'

        json_base = json.loads(json1)
        print(json_base)


        card_group = json_base['card_group']
        # print(len(card_group))
        for num in range(0, len(card_group)):
            member = card_group[num]
            print(member['member']['id'])
            print(print(member['member']['screen_name']))

            postData2 = {"uid": member['member']['id'], 'st': '6e7e13'}  # post请求传的数据
            url = 'https://m.weibo.cn/api/friendships/create'
            # https: // m.weibo.cn / api / friendships / create
            respone1 = requests.post(url, data=postData2, headers=headetr2,verify=False)
            print(respone1.text)
            json_str = respone1.content

            # print(json_str.decode('gbk').encode('utf-8').decode('unicode_escape'))
        #
            time.sleep(10)

    time.sleep(30)
guanzhugroup(1)
    # https://m.weibo.cn/groupChat/userChat/groupMembers?group_id=4197189808619503