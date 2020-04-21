
arr=[]
count=0
with open("rand.txt") as file:
	for number in file:
		line = '{0:08X}'.format(int(number))
		arr.append(line)
		count=count+1
		if count%10 == 0:
			f = open("out.txt", "a")
			f.write("".join(arr)+"\n")
			arr=[]
