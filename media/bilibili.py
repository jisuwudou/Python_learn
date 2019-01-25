# https://www.bilibili.com/video/av38370242?from=search&seid=16199216392611206040

import requests
import urllib3
import re
import json
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://www.bilibili.com'}

url1 = 'https://www.bilibili.com/video/av38370242?from=search&seid=16199216392611206040'


def getvideourls(url):
    sessioin = requests.session()
    req = sessioin.get(url, verify=False, headers=headers)

    pattern = '.__playinfo__=(.*)</script><script>window.__INITIAL_STATE__='
    try:
        infos = re.findall(pattern, req.text)[0]
    except Exception as e:
        print(e)
        return []
    json_ = json.loads(infos)
    durl=''
    if 'durl' in json_:
        durl = json_['durl']
    else:
        durl = json_['data']['durl']
    print(durl)


getvideourls(url1)
