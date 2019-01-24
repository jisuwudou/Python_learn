from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.set_window_size(1300,1300)
browser.get('https://passport.douyu.com/member/login?')
time.sleep(1)
test = browser.find_element_by_id('loginbox-con')

print(test)
changeelm = browser.find_element_by_class_name("js-qrcode-switch")
print(changeelm)
changeelm.click()

#切换到昵称输入
email_elem = browser.find_element_by_css_selector("[class='l-stype js-l-stype']")
print(email_elem)
email_elem.click()
email_elem = browser.find_element_by_name('username')        #查找name属性值为'email'的元素
print(email_elem)
email_elem.send_keys('jisuwudou')                 #调用send_keys()方法，填写账号
password_elem = browser.find_element_by_name('password')  #查找name属性值为'password'的元素
password_elem.send_keys('yang3386')                          #填写密码
print(password_elem.tag_name)
do_login = browser.find_element_by_class_name("loginbox-sbt")          #查找登录按钮的元素
print(do_login.tag_name)
do_login.click()                                          #模拟鼠标点击登录按钮
print('Done!')
# ---------------------
# 作者：酱豆腐
# 来源：CSDN
# 原文：https://blog.csdn.net/simplelearner/article/details/81947215
# 版权声明：本文为博主原创文章，转载请附上博文链接！