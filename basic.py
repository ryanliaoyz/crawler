#coding=utf-8
#-*- coding: utf-8 -*-

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com") #urlopen(url, data, timeout) 
print(response.read())
