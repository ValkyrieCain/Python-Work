no=[1,2,3,4,5,6,7,8,9,10]
string=""
count=0
while count<10:
	if count<1:
		string+=str(no[count])
		print(string,".")
		count+=1
	else:
		string+=","+str(no[count])
		print(string,".")
		count+=1