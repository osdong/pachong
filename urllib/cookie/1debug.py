#coding:utf8

import urllib2
#打开 HTTP debug log
httpHandler = urllib2.HTTPHandler(debuglevel=1)
#打开 HTTPS debug log
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

#同时使用两种不同的 debug log 模式

opener = urllib2.build_opener(httpHandler,httpsHandler)

urllib2.install_opener(opener=opener)

response = urllib2.urlopen("https://www.renren.com")
print response