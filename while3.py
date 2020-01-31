From=int(input("Times table from? "))
To=int(input("Times table to? "))
while From<=To:
	a=1
	print("Times table of",From)
	print("-------------------")
	while a<=10:
		print(From,"x",a,"=",From*a)
		a+=1
	From+=1