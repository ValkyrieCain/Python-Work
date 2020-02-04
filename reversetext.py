msg=input("Enter a message: ")
word=""
final=""
i=0
while i<len(msg):
	if msg[i]==" ":
		final=final+word+" "
		word=""
	else:
		word=msg[i]+word
	i+=1
final=final+word
print(final)