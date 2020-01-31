no=int(input("4 digits "))
a=int(no/1000)
b=(int(no/100))%10
c=(int(no/10))%10
d=no%10
print(a,"+",b,"+",c,"+",d,"=",a+b+c+d)