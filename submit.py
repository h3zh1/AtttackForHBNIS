import requests
import string

def submitflag(flag) : 
    #填提交flag的地址
    print("hello")
    url  = "http://127.0.0.1:8088/compete_record/"
    #对应的参数形式
    data = { "compete_answer" : { "flag" : flag }  }
    #headr中亮神记得根据抓包写一下Cookies,多个Cookie以分好';'分隔,
    headers = {
        "Cookies":"sessionid=fqopuoyttrfbx6ondrefdgpfkdmifgj2;cookie2=123;"
        }
    #当时我们交flag是用json交的 , get和post那种正常数据就不写了你酌情改
    r = requests.post(url , json=data , headers = headers)
    

