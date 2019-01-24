# -*- coding:utf-8 -*-
import socket
import re
import time
import struct
import threading

def connect():
    '''
    第三方客户端通过 TCP 协议连接到弹幕服务器(依据指定的 IP 和端口);
    第三方接入弹幕服务器列表:
    IP 地址:openbarrage.douyutv.com 端口:8601
    '''
    print('-----*-----DouYu_Spider-----*-----\n')
    host = socket.gethostbyname("openbarrage.douyutv.com")
    port = 8601
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

def send_msg(msg):
    data_length = len(msg) + 8
    code = 689
    msgHead = struct.pack('<i',data_length) \
          + struct.pack('<i',data_length) + struct.pack('<i',code)
    s.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = s.send(msg[sent:])
        print("send %d tn=%d",sent,tn,threading.currentThread())
        sent = sent + tn

def danmu(room_id):
    '''
    1.客户端向弹幕服务器发送登录请求
    2.客户端收到登录成功消息后发送进入弹幕分组请求给弹幕服务器
    '''
    login = 'type@=loginreq/roomid@=%s/\0'%room_id
    login = login.encode('utf-8')
    send_msg(login)
    joingroup = 'type@=joingroup/rid@=%s/gid@=-9999/\0'%room_id
    joingroup = joingroup.encode('utf-8')
    send_msg(joingroup)
    while True:
        content = s.recv(1024)

        if judge_chatmsg(content):
            nickname = nick_name(content)
            chatmsg = chat_msg(content)
            if chatmsg:
                print(chatmsg)
                print('%s : %s' % (nickname, chatmsg))
            # print('%s : %s'%(nickname,chatmsg))
        else:
            print(content)
            pass


def keep_alive():
    '''
    客户端每隔 45 秒发送心跳信息给弹幕服务器
    '''
    while True:
        msg = 'type@=keeplive/tick@=%s/\0'%str(int(time.time()))
        send_msg(msg.encode('utf-8'))
        time.sleep(45)

def nick_name(content):
    '''
    弹幕消息：
    type@=chatmsg/rid@=301712/gid@=-9999/uid@=123456/nn@=test /txt@=666/level@=1/
    判断type，弹幕消息为chatmsg，txt为弹幕内容，nn为用户昵称
    '''
    # pattern = re.compile(r'nn@=(.*)/txt@')
    # nickname = pattern.findall(content)[0]
    return 'nickname'

def chat_msg(content):
    '''
    弹幕消息：
    type@=chatmsg/rid@=301712/gid@=-9999/uid@=123456/nn@=test /txt@=666/level@=1/
    判断type，弹幕消息为chatmsg，txt为弹幕内容，nn为用户昵称
    '''
    pattern = re.compile(r'txt@=(.*)/cid@')
    chatmsg = pattern.findall(str(content))
    len(chatmsg)
    if len(chatmsg) > 0:
        chatmsg = chatmsg[0]
    else:
        chatmsg = None
    return chatmsg

def judge_chatmsg(content):
    '''
    判断是否为弹幕消息
    '''
    return True
    # pattern = re.compile(r'type@=(.*)/rid@')
    # data_type = pattern.findall(content)
    # try:
    #     if data_type[0] == 'chatmsg':
    #         return True
    #     else:
    #         return False
    # except Exception as e:
    #     return False



if __name__ == '__main__':
    connect()
    t1 = threading.Thread(target=danmu,args=(2947432,))
    t2 = threading.Thread(target=keep_alive)
    t1.start()
    t2.start()

# 作者：Awesome_Tang
# 链接：https://www.jianshu.com/p/fbc08945fa01
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。