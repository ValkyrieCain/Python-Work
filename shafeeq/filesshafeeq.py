read=open("data.txt")
write=open("data2.txt","w")
word=""
for line in read:
	for x in line:
		if x=="e" or x=="E":
			print("*",end="",file=write)
		else:
			print(x,end="",file=write)