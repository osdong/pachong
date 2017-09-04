#coding:utf8

import requests


cookie = dict(BDORZ="27325 for .baidu.com")
req = requests.get(url="http://www.baidu.com",cookies = cookie)

print req.cookies