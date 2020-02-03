msg=input("Enter a message: ")
word=""
char1=len(msg)-1
while char1>0:
	if msg[char1]==" ":
		char2=char1+1
		while char2<len(msg):
			if msg[char2]==" ":
				break
			word=word+msg[char2]
			char2+=1
		print(word)
		word=""	
	char1-=1
char1=0
while msg[char1]!=" ":
	word=word+msg[char1]
	char1+=1
print(word)