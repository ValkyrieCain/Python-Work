msg=input("Enter a message: ")
word=""
i=len(msg)-1
while i>-1:
	if msg[i]==" ":
		print(word)
		word=""
	else:
		word=msg[i]+word
	i-=1
print(word)