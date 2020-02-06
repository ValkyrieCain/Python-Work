length=int(input("How many steps do you want? "))
numbers={}
string=""
counter=0
while counter<length:
	numbers[counter]=counter+1
	if counter<1:
		string+=str(numbers[counter])
	else:
		string+=","+str(numbers[counter])
	print(string,".")
	counter+=1