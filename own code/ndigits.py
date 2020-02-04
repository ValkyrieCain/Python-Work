no=input("n digits ")
d={}
length=len(no)
var=1
dfinal=""
dtotal=0
while length>1:
	d[var]=int(no[var-1])
	dfinal=dfinal+str(d[var])+" + "
	dtotal+=d[var]
	length-=1
	var+=1
d[var]=int(no[var-1])
dfinal=dfinal+str(d[var])
dtotal+=d[var]
print(dfinal,"=",dtotal)