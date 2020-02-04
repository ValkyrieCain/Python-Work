no=input("Sum of digits: ")
d={}
length=len(no)
var=1
dtotal=0
while length>1:
	d[var]=int(no[var-1])
	print(d[var],"+ ",end="")
	dtotal+=d[var]
	length-=1
	var+=1
d[var]=int(no[var-1])
dtotal+=d[var]
print(d[var],"=",dtotal)