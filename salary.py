name=input("Please enter your name ")
salary=int(input("Please enter your salary "))
if salary<=11000:
	tax=0
else:
	tax=(salary-11000)*20/100
net=salary-tax
print("Salary Slip of",name)
print("Salary =",salary)
print("Tax =",tax)
print("Net Salary =",net)
