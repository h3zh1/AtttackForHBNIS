import requests
import string

success_sign = "[+ success +]"
failed_sign  = "[- fail    -]"
error_sign   = "[- error   -]"

def subFlagByJson( flagData , sub_url , sub_header) :
    r = requests.post(sub_url , json = flagData , headers = sub_header)
    return r
def subFlagByGet(  flagData , sub_url , sub_header) : 
    r = requests.get(sub_url , params = flagData , headers = sub_header)
    return r
def subFlagByPost( flagData , sub_url , sub_header) :
    r = requests.post(sub_url , data = flagData , headers = sub_header)
    return r
    
def subflag( flag_target, flag , sub_url , sub_header  ,subMethod ) :  
    """[summary]
    Args:
        flag_target (UrlString): 靶机地址
        flag (String): 拿到的flag
        sub_url (UrlString]): Flag校验地址
        sub_header (HTTP_headers): HTTP头保存状态
        subMethod (HTTP_Method): 提交方法
    """
    switcher = { "POST": subFlagByPost, "GET": subFlagByGet, "JSON": subFlagByJson }
    # 失败的消息
    failed_list = []
    # 错误消息
    error_list = []
    try :    
        res = switcher.get( subMethod , subFlagByJson )( flag , sub_url , sub_header )
        # print(res.text)
        if "success" in res.text :
            print( "{0} Target : [ {1} ] Flag:[ {2} ] ".format( success_sign , flag_target , flag ) )
        else :
            failed_list.append( "{0} Target : [ {0} ] Flag:[ {1} ] ".format( flag_target , flag ) )
    except :
        error_list.append("[- error  -] Target : [ {0} ] Flag:[ {1} ] ".format( error_sign ,flag_target , flag) )
        pass   
    
    for i in failed_list :
        print(i) 
    
    for i in error_list : 
        print(i)
