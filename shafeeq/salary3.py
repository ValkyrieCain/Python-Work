name=input("Enter your name: ")
salary=int(input("Enter your salary: "))
if salary>=3000:
	tax=salary*35/100
if salary>=2000 and salary<3000:
	tax=salary*25/100
if salary>=1000 and salary<2000:
	tax=salary*15/100
if salary<1000:
	tax=0