string=input("Enter any string: ")
length=len(string)
position=0
character=""
answer=""
while position<length:
	character=string[position]
	if ord(character)>=48 and ord(character)<=57:
		answer=answer+str(int(character)*2)
	elif ord(character)>=65 and ord(character)<=90:
		answer=answer+chr(ord(character)+32)
	elif ord(character)>=97 and ord(character)<=122:
		answer=answer+chr(ord(character)-32)
	else:
		answer=answer+character
	character=""
	position+=1
print(answer)