no=int(input("5 digits "))
a=int(no/10000)
b=(int(no/1000))%10
c=(int(no/100))%10
d=(int(no/10))%10
e=no%10
print(a,"+",b,"+",c,"+",d,"+",e,"=",a+b+c+d+e)