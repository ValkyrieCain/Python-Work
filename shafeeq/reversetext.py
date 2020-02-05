msg=input("Enter a message: ")
word=""
final=""
pos=0
while pos<len(msg):
	if msg[pos]==" ":
		final=final+word+" "
		word=""
	else:
		word=msg[pos]+word
	pos+=1
final=final+word
print(final)