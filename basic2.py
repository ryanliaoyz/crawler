#coding=utf-8
#-*- coding: utf-8 -*-

import urllib.request

request = urllib.request.Request("http://www.baidu.com") #request object
response = urllib.request.urlopen(request) #same result
print (response.read()) 
