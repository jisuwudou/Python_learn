import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 登录后才能访问的网页
url = 'https://www.douyu.com/directory/myFollow'

# 浏览器登录后得到的cookie，也就是刚才复制的字符串
# cookie_str = r'acf_devid=dee5fd49dc0ee09ec7eb4b0e2a847b4a; dy_did=c2d3a8eefb7db2645fd07d5500001501; acf_did=c2d3a8eefb7db2645fd07d5500001501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1547607235; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1547608113; smidV2=201901161108322c9f4a53756293a97583b9c90c9a58f300ed2e547b80d3310; PHPSESSID=a577cvttnac5agro1tmla2bai5; acf_auth=eb42pYSWe9NOR%2FdnCkS2HOAzX0YvAlsGmhoGAfcLa27gTPpNnBvXi3lVBxpVK2DnlnAltOa1YYgoDghDrYfGgk2DfW5GVdhxME1k%2FlA908iYGSNTPR1xkHX0X9%2Bvzw; wan_auth37wan=caa88c1c93bcFR4aJS9VtpCnqtHIXp0QPhZMp7vOdzOQZaSg1LHkNzJ3OOe2zZ0tfvxNgkF65N5rEA8qENDMkOthTWvCbpSpv%2F8vzQmJieZKMulcEQ; acf_uid=11301303; acf_username=auto_mbSDo9P6Z7; acf_nickname=jisuwudou; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F011%2F30%2F13%2F03_avatar_; acf_ct=0; acf_ltkid=93663713; acf_biz=1; acf_stk=d73cf7a247fe28d3'
# cookie_str = r'a=1;b=2;c=3'
cookie_str = r'acf_devid=dee5fd49dc0ee09ec7eb4b0e2a847b4a; dy_did=c2d3a8eefb7db2645fd07d5500001501; acf_did=c2d3a8eefb7db2645fd07d5500001501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1547607235; smidV2=201901161108322c9f4a53756293a97583b9c90c9a58f300ed2e547b80d3310; PHPSESSID=a577cvttnac5agro1tmla2bai5; acf_auth=ae75N0gNHtVDQmMTBYG%2BOfveAzThmBiKDMM3bgi8my2V4EAkgL0Xd2lK8qmca%2F4MzHwWjTeuvsGrz3fAVPg3fHM0Oi8qWGC7dM5hIAcjf253FgmAmupDQUA73y3uTA; wan_auth37wan=1fa2f4c177b8IeZ%2Bjj2kKd%2BcNv01rM%2Fa8HF9Fd1T2b%2BN6mwjdh072pkr12BJpwWlP0G5nA65EGjATzTfGoDMQ%2BLrK%2BP2j43LgtPa0n6ML1LLQEL7Hw; acf_uid=11301303; acf_username=auto_mbSDo9P6Z7; acf_nickname=jisuwudou; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F011%2F30%2F13%2F03_avatar_; acf_ct=0; acf_ltkid=93663715; acf_biz=1; acf_stk=42dbac13d453c0ff; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1547609683'
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 设置请求头
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# 在发送get请求时带上请求头和cookies
resp = requests.get(url, headers=headers, cookies=cookies,verify=False)

print(resp.content.decode('utf-8'))
"""
{
	"d": "c2d3a8eefb7db2645fd07d5500001501",
	"i": "11301303",
	"rid": 0,
	"u": "/directory/myFollow",
	"ru": "/directory/myFollow",
	"ac": "init_page_live",
	"rpc": "page_live",
	"pc": "page_live",
	"pt": 1547608172335,
	"oct": 1547608172497,
	"dur": 0,
	"pro": "host_site",
	"ct": "web",
	"e": {
		"domr": 1,
		"ut": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
		"chan_code": null,
		"duration": 128,
		"ice": 0,
		"tid": 0,
		"cid": 0,
		"name": "我的关注",
		"rac": "show_page_staydur",
		"t_stamp": 1547608172000,
		"br_nv": "chrome/71.0.3578.98",
		"br_l": "zh-CN",
		"supp_ck": 1,
		"sys_vt": "Windows7",
		"scr_rw": 1920,
		"scr_rh": 1080,
		"br_w": 1920,
		"br_h": 1040,
		"html_w": 729,
		"html_h": 925,
		"ws_x": 0,
		"ws_y": 0,
		"sc_c": "x64",
		"scr_sw": 729,
		"scr_sh": 925,
		"version": "2.0",
		"lage": "zh-CN",
		"lages": "zh-CN,zh",
		"tzone": -480,
		"isse": 1,
		"iude": 1,
		"ca": "x64"
	},
	"av": "",
	"up": ""
}



acf_devid=dee5fd49dc0ee09ec7eb4b0e2a847b4a; dy_did=c2d3a8eefb7db2645fd07d5500001501; acf_did=c2d3a8eefb7db2645fd07d5500001501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1547607235; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1547608113; smidV2=201901161108322c9f4a53756293a97583b9c90c9a58f300ed2e547b80d3310; PHPSESSID=a577cvttnac5agro1tmla2bai5; acf_auth=eb42pYSWe9NOR%2FdnCkS2HOAzX0YvAlsGmhoGAfcLa27gTPpNnBvXi3lVBxpVK2DnlnAltOa1YYgoDghDrYfGgk2DfW5GVdhxME1k%2FlA908iYGSNTPR1xkHX0X9%2Bvzw; wan_auth37wan=caa88c1c93bcFR4aJS9VtpCnqtHIXp0QPhZMp7vOdzOQZaSg1LHkNzJ3OOe2zZ0tfvxNgkF65N5rEA8qENDMkOthTWvCbpSpv%2F8vzQmJieZKMulcEQ; acf_uid=11301303; acf_username=auto_mbSDo9P6Z7; acf_nickname=jisuwudou; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F011%2F30%2F13%2F03_avatar_; acf_ct=0; acf_ltkid=93663713; acf_biz=1; acf_stk=d73cf7a247fe28d3

"""