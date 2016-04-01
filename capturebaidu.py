#encoding:UTF-8
import urllib2
 
url = "http://www.baidu.com"
data = urllib2.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

