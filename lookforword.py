msg=input("Enter a message: ")
findword=input("Word to look for: ")
word=""
position=0
counter=0
while position<len(msg):
	word=word+msg[position]
	if word[0]==findword[0]:
		search=position
		while len(word)<len(findword):
			search+=1
			if search==len(msg):
				break
			word=word+msg[search]
		if word==findword:
			counter+=1
		word=""
	else:
		word=""
	position+=1
if counter==1:
	print("The word",findword,"appeared",counter,"time.")
else:
	print("The word",findword,"appeared",counter,"times.")