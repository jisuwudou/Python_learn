import urllib
re = urllib.request.urlopen("https://blog.csdn.net/samsam2013/article/details/78492122")
doc = open("web_info.txt","w")
print(re.read(),file = doc)
print(re.read())