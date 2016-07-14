# test_client.py
#coding=utf-8
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

# 在 urllib2 上注册 http 流处理句柄
register_openers()

# 开始对文件 "DSC0001.jpg" 的 multiart/form-data 编码
# "image1" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置

# headers 包含必须的 Content-Type 和 Content-Length
# datagen 是一个生成器对象，返回编码过后的参数
params = {'file':open('/root/libpcap-1.7.4.tar.gz', "rb") }
datagen, headers = multipart_encode(params)
req_url = 'http://192.168.24.187:8080/upload'
request = urllib2.Request(req_url, datagen, headers)
response_data = urllib2.urlopen(request)
print urllib2.urlopen(request).read()
