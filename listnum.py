n=[1,2,3,4,5,6,7,8,9,10]
m=""
v=0
while v<10:
	if v<1:
		m+=str(n[v])
		print(m,".")
		v+=1
	else:
		m+=","+str(n[v])
		print(m,".")
		v+=1