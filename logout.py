#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, re

def logout(url="http://gw.bupt.edu.cn/F.html"):
    response = urllib2.urlopen(url)
    rsp = response.read()
    temp = re.findall(r"Msg=(\d+)", rsp)[0]
    if temp=='14':
        print "注销成功"
    elif temp=='01':
        print "尚未登录"
    else:
        print "注销失败"

logout()
