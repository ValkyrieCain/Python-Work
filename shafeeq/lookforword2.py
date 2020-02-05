msg=input("Enter a message: ")
findword=input("Word to look for: ")
counter=0
for findword in msg:
	counter+=1
print("The word",findword,"appeared",counter,"times.")