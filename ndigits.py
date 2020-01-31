no=int(input("n digits "))
def digits():
	import math
	digits=int(math.log10(no))+1
digits()
d1z="1"
while digits!=1:
	d1z=(d1z+"0")
	digits=digits-1
d1=int(no/int(d1z))
digits()
d2z=1
while digits!=2:
	d2z=(d2z+"0")
	digits=digits-1
d2=(int(no/int(d2z)))/10
digits()
b=(int(no/1000))%10
c=(int(no/100))%10
d=(int(no/10))%10
d5=no%10
print(d1,"+",d2,"+",d3,"+",d4,"+",d5,"=",d1+d2+d3+d4+d5)