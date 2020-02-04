names=[input("Enter name 1 "),"Valkyrie","Francis"]
for x in names:
	for z in x:
		if ord(z)>=97 and ord(z)<=122:
			print(chr(ord(z)-32))
		elif ord(z)>=65 and ord(z)<=90:
			print(chr(ord(z)+32))
		else:
			print(z)
