import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
# https://www.cnblogs.com/malcolmfeng/p/6854967.html
browser = webdriver.Chrome()
browser.get('http://weibo.com')
time.sleep(10)

# 点击页面中的登录按钮 弹出输入帐号模态框
browser.find_element_by_xpath("//a[@node-type='loginBtn']").click()
time.sleep(2)

# 输入帐号密码
browser.find_element_by_css_selector('div.item.username.input_wrap input.W_input').send_keys('2952450200@qq.com ')
browser.find_element_by_css_selector('div.item.password.input_wrap input.W_input').send_keys('Yang3386')
time.sleep(1)

# 点击登录
browser.find_element_by_xpath("//div[@class='item_btn']/a[@suda-data='key=tblog_weibologin3&value=click_sign']").click()
time.sleep(5)

# jsCode = "var q=document.documentElement.scrollTop=10"
# browser.execute_script(jsCode)
# print("拖动滑动条到底部...")
browser.maximize_window()#不放大，move_to_element会对不上位置

for i in range(0, 2):
    jsCode = "var q=document.documentElement.scrollTop="+str((i+1) * 10000)
    browser.execute_script(jsCode)
    print(i)
    time.sleep(3)

jsCode = "var q=document.documentElement.scrollTop=0"
browser.execute_script(jsCode)

# 查找页面中的所有 点赞按钮
allzan = browser.find_elements_by_css_selector('.W_ficon.ficon_praised.S_txt2')

for temp in allzan:
    print("again")
    ActionChains(browser).move_to_element(temp).perform()#看不见的，不可以点击
    time.sleep(5)
    temp.click()


