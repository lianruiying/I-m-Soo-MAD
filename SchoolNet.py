#!/usr/bin/python
# -*- coding: utf-8 -*-

import HTMLParser
import urllib2
import urlparse
import cookielib
import string
import re
import urllib

#登陆主页面
link = 'http://172.20.3.81:801/srun_portal_pc.php?ac_id=3&cmd=login&switchip=192.168.71.3&mac=b4:ae:2b:3b:29:b1&ip=172.21.188.180&essid=ECUST&apname=FX-TWXX-4F-W02&apgroup=fx-free-apgroup-jiaoxue&url=http%3A%2F%2Fgo%2Emicrosoft%2Ecom%28null%29'
#post页面   (待定）
posturl = 'http://172.20.3.81:801/include/auth_action.php'
#cookie处理器
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
#下载cookie
local = urllib2.urlopen(link)

#构造header和post
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Referer': 'http://172.20.3.81:801/srun_portal_pc.php?ac_id=3&cmd=login&switchip=192.168.71.3&mac=b4:ae:2b:3b:29:b1&ip=172.21.188.180&essid=ECUST&apname=FX-TWXX-4F-W02&apgroup=fx-free-apgroup-jiaoxue&url=http%3A%2F%2Fgo.microsoft.com%28null%29'}

postData = {  
    'ac_id':'13' ,   
    'action':'login' ,
    'nas_ip': ' ' ,
    'password': '{B}NjAxNjMy',
    'user_ip': '172.21.188.180',
    'user_mac' : 'b4:ae:2b:3b:29:b1',
    'username' : '10163698@free'
}
    
    
#Post编码
postData = urllib.urlencode(postData)
#数据
request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text    