import os
path = "E:\python\\test"
file = path + "/" + "1.txt.txt"

f=open(file,'r')
a_list=[]
line = f.readline()
while line:
	line = line.strip('\n')
	a=line.split('\t')
	a_list.append(a[1])
	print(a_list)
	line = f.readline()

f.close()