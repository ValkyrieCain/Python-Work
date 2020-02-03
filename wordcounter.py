message=input("Enter a message: ")
space=1
i=0
while i<len(message):
	if message[i]==" ":
		space+=1
	i+=1
print("In the message there are",space,"words.")