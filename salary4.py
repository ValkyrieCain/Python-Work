name=input("Enter your name: ")
salary=int(input("Enter your salary: "))
if salary>=3000:
	tax=salary*35/100
	print("tax=35%")
if salary>=2000 and salary<3000:
	tax=salary*25/100
	print("tax=25%")
if salary>=1000 and salary<2000:
	tax=salary*15/100
	print("tax=15%")
if salary<1000:
	tax=0
	print("tax=0%")
print("tax=",tax)
print("salary=",salary)
print("net salary=",salary-tax)