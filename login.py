import urllib
import urllib2
import hashlib
def login(url, usr, pwd):
    data = {}
    data["DDDDD"] = usr
    data["upass"] = calpwd(pwd)
    data["R1"] = "0"
    data["R2"] = "1"
    data["para"] = "00"
    data["0MKKey"] = "123456"
    req=urllib2.Request(url)
    data = urllib.urlencode(data)
    data
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    response.read()
  
def calpwd(init_pwd):
    pid = '1'
    calg='12345678'
    tmp = pid + init_pwd + calg
    pwd = hashlib.md5(tmp).hexdigest() + calg + pid
    return pwd
  
  
login("http://10.3.8.211", "学号", "密码") 
