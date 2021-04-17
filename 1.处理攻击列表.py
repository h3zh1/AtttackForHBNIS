#读ip文件
file1 = open("/Users/h3zh1/Desktop/自写awd/ip.txt","r")
file2 = open("/Users/h3zh1/Desktop/自写awd/lastest_ip.txt","w")
rows = file1.readlines()

for i in rows:
    if i != "\n":
        file2.writelines(i)
        print(i)
file2.close()
        
    