#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys
import json
import time

import re
import urllib3#不显示ssh验证的提示，不管也行

urllib3.disable_warnings()#不显示ssh验证的提示，不管也行urllib3.disable_warnings()
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_T_WM=7bc53011a8a353cb26566c6a96ac5907; SCF=AuBHnIuNmm18bBJyhNt2aDXMrQpmsUw7JNh3HTgfHYmcxS5v2oPPdxuaDDiRTeNTx9n-UiPq2gUgeJD8WBhqj2o.; MLOGIN=1; SUB=_2A25xUCoTDeRhGeNP7lQU9inFyz6IHXVSurZbrDV6PUJbkdAKLVPxkW1NTm4vJR0bdEH7g8w2oYVvEIpuLmJoI3Lt; SUHB=0mxEXSSYuc_n-K; SSOLoginState=1549032003; WEIBOCN_FROM=1110005030; M_WEIBOCN_PARAMS=oid%3D4334988801699578%26luicode%3D10000011%26lfid%3D1076036745121439%26fid%3D1076036963955244%26uicode%3D10000011; XSRF-TOKEN=0561f7',#步骤2.4登录微博后找到requestheader里的cookie
        'Host': 'm.weibo.cn',
        'RA-Sid': 'B781E81A-20150402-024118-ce25e1-ba5345',
        'RA-Ver': '3.0.8',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36',
        'Referer': 'https://m.weibo.cn/message',
    }

def guanzhugroup(groupid):

    for nums in range(20, 49):  # 这里是模拟页数，在获取groupMembersList的返回信息里有max_pageprint('***************第几页='+str(nums))
        print('***************第几页='+str(nums))

        urluser = "https://m.weibo.cn/groupChat/userChat/groupMembersList?group_id=%s&page=%d" % (groupid, nums)

        respone = requests.get(urluser, headers=headers, verify=False)

        # print(respone)
        print(respone.text)
        pattern = re.compile('\['+'(.*?)'+']',re.S)
        json1 = pattern.findall(respone.text)[0]+']}'

        json_base = json.loads(json1)
        print(json_base)

        card_group = json_base['card_group']

        st_url = 'https://m.weibo.cn/api/config/'
        st_respone = requests.post(st_url, headers=headers, verify=False)
        st_json = json.loads(st_respone.content)
        print('st = ' + st_json['data']['st'])

        # print(len(card_group))
        for num in range(0, len(card_group)):
            member = card_group[num]
            print("*********************** next member ************************************************")
            print(member['member']['id'])
            print(member['member']['screen_name'])

            postData2 = {"uid": member['member']['id'], 'st': st_json['data']['st']}  # post请求传的数据
            url = 'https://m.weibo.cn/api/friendships/create'

            respone1 = requests.post(url, data=postData2, headers=headers,verify=False)
            respone1_json = json.loads(respone1.content)
            if respone1_json['ok'] == 0:
                if 'errno' in respone1_json.keys():
                    print("****错误码："+str(respone1_json['errno']))
                    time.sleep(2)
                continue
            print("create respone = "+respone1.text)
            json_str = respone1.content

            chatgroup_url = 'https://m.weibo.cn/groupChat/userChat/chat?group_id=' + str(groupid)
            chatgroup_respone = requests.get(chatgroup_url, headers=headers, verify=False)
            # print(chatgroup_respone.text)

            try:

                chat_st = re.search(r'\"st\":\"(\w+)\"', chatgroup_respone.text)

                chat_st_param = chat_st.group().split('"')[3]#在群里发消息需要的参数st，注意和关注的st参数不一样


                sendmsg_url = 'https://m.weibo.cn/groupChat/userChat/sendMsg'
                sendmsg_data = {
                    'content': '@%s 我关注你了' % member['member']['screen_name'],#这里的@没有实际的@功能，电脑上不太好@，不知道实际的@发的是什么。还在研究用手机设置代理或者安卓模拟器抓个包试试
                    'st': chat_st_param,
                    'group_id': groupid,
                }
                sendmsg_respone = requests.post(sendmsg_url, headers=headers, data=sendmsg_data, verify=False)
                print('send msg ret = '+sendmsg_respone.text)

            except Exception as e:
                print(e)

            time.sleep(30)

    time.sleep(60)

guanzhugroup(4075182799395477)



