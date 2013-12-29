import urllib2
def logout(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req)
  
logout("http://gw.bupt.edu.cn/F.html") 
