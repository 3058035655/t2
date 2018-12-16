import urllib.request
req = urllib.request.urlopen('http://www.imooc.com/course/list')

buf = req.read()
buf=buf.decode('utf-8')
print (buf)
import re

listurl =re.findall(r'http:.+\.jpg',buf)
print (listurl)
i=0
for url in listurl:
    f = open(str(i)+'.jpg','w')
    req = urllib.request.urlopen("http://www.imooc.com/course/list")
    buf = req.read()
    buf=buf.decode('utf-8')
    f.write(buf)
    i+=1

