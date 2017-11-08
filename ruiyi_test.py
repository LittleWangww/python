import os  

path = "E:\python\\ruiyitest"
file1 = path + "/" + "sample1.txt"
file2 = path + "/" + "sample2.txt"
file3 = path + "/" + "sample3.txt"
of = "result.txt"
oof = "result_sort.txt"
object1=open(of,'w')
object2=open(oof,'w')

list1={}
list2={}
list3={}
total_list=[]
f1 = open(file1)
line1 = f1.readline()
while line1:
	array = line1.split("\t")
	array[1] = array[1].strip('\n')
	if array[0] not in total_list:
		total_list.append(array[0])
	list1[array[0]] = float(array[1])
	#print(float(array[1]))
	line1 = f1.readline()
f1.close()

#print(total_list)

f2 = open(file2)
line2 = f2.readline()

while line2:
	array = line2.split("\t")
	array[1] = array[1].strip('\n')
	if array[0] not in total_list:
		total_list.append(array[0])
	list2[array[0]] = float(array[1])
	line2 = f2.readline()
f2.close()

f3 = open(file3)
line3 = f3.readline()

while line3:
	array = line3.split("\t")
	array[1] = array[1].strip('\n')
	if array[0] not in total_list:
		total_list.append(array[0])
	list3[array[0]] = float(array[1])
	line3 = f3.readline()
f3.close()

dict_total={}
sumnum=0
for gene in total_list:
	if gene not in list1.keys():
		list1[gene] = 0
	if gene not in list2.keys():
		list2[gene] = 0
	if gene not in list3.keys():
		list3[gene] = 0
	sumnum=list1[gene]+list2[gene]+list3[gene]
	dict_total[gene]=sumnum

object1.write("Geneid\tSam1\tSam2\tSam3\n")
for gene in dict_total.keys():
	string = gene + "\t" + str(list1[gene]) + "\t" + str(list2[gene]) + "\t" + str(list3[gene]) + "\n"
	object1.write(string)

sortdict = dict(sorted(dict_total.items(), key = lambda x: x[1]))

object2.write("Geneid\tSam1\tSam2\tSam3\n")
for gene in sortdict.keys():
	string = gene+"\t"+str(list1[gene])+"\t"+str(list2[gene])+"\t"+str(list3[gene])+ "\n"
	object2.write(string)

object1.close()
object2.close()
