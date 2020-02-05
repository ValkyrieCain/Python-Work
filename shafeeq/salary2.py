name=input("Please enter your name ")
salary=int(input("Please enter your salary "))
if salary>2000:
	tax=salary*21/100
	net=salary-tax
else:
	tax=salary*15/100
	net=salary-tax
print("tax=",tax)
print("net=",net)