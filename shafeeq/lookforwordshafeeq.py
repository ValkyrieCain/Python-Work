msg=input("Enter a message: ")
findword=input("String to look for: ")
position=0
counter=0
while position<len(msg):
	if msg[position]==findword[0]:
		if msg[position:position+len(findword)]==findword:
			counter+=1
	position+=1
if counter==1:
	print("The string",findword,"appeared",counter,"time.")
else:
	print("The string",findword,"appeared",counter,"times.")