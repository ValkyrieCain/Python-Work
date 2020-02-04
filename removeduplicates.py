msg=input("Enter a message: ")
word=""
final=""
pos=0
while pos<len(msg):
	if msg[pos]==" ":
		if word in final:
			pass
		else:
			final=final+word+" "
		word=""
	else:
		word+=msg[pos]
	pos+=1
if word in final:
	pass
else:
	final=final+word
print(final)