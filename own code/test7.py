no=input("n digits ")
d={
1:0,
2:0,
3:0,
4:0,
5:0,
6:0,
7:0,
8:0,
9:0}
dtotal=d[1]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9]
length=len(no)
var=1
while length>1:
	d[var]=int(no[var-1])
	print(d[var],"+")
	length-=1
	var+=1
d[var]=int(no[var-1])
dtotal=d[1]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9]
print(d[var],"=",dtotal)