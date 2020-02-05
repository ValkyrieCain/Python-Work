read=open("data.txt")
write=open("data2.txt","w")
word=""
for line in read:
	for x in line:
		if x=="e":
			word+="*"
		else:
			word+=x
	print(word,file=write)
	word=""