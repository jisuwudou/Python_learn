import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
# data = {'Login.Token1':'学号',
#         'Login.Token2':'密码',
#         'goto:http':'//ssfw.xmu.edu.cn/cmstar/loginSuccess.portal',
#         'gotoOnFail:http':'//ssfw.xmu.edu.cn/cmstar/loginFailure.portal'}
data = {
    'ver': '1103',
    'roomid': '0',
    'cate1': 'null',
    'cate2': 'null',
    'posid': '1,2,24,62,23',
    'uid': '11301303',
}

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://rtbapi.douyucdn.cn/japi/sign/web/getinfo'

#构造Session
session = requests.Session()
print(session.cookies.get_dict())
#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)

#登录后才能访问的网页
url = 'https://www.douyu.com/directory/myFollow'

#发送访问请求
resp = session.get(url)

print(resp.content.decode('utf-8'))