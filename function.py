def addition(a,b):
	result=a+b
	print(a,"+",b,"=",result)
addition(10,20)
no1=int(input("first number: "))
no2=int(input("second number: "))
addition(no1,no2)
def tax(salary):
	t=salary*21/100
	return t
s=int(input("Enter your salary: "))
print("Your tax is",tax(s))
print("Your net salary is",(s-tax(s)))
if tax(s)>500:
	print("Oops, too much tax!")
print(addition(tax(s),tax(s)))
print(tax(tax(s)))