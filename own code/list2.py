dz={
1:0,
2:0,
3:0,
4:0,
5:0,
6:0,
7:0,
8:0,
9:0}
no=(input("n digits "))
length=len(no)
var=1
while length>0:
	dz[str(var)]=10**length
	length=length-1
	var=var+1
print(dz)