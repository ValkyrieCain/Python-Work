no=int(input("n digits "))
import math
digits=int(math.log10(no))+1
print(digits)
a="1"
while digits!=1:
	a=(a+"0")
	digits=digits-1
print(a)
b=(int(no/1000))%10
c=(int(no/100))%10
d=(int(no/10))%10
e=no%10
print(a,"+",b,"+",c,"+",d,"+",e,"=",b+c+d+e)