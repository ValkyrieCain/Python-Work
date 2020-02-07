name=""
longest=""
while name!="0":
	name=input("Enter a name: ")
	if len(name)>len(longest):
		longest=name
print("Longest name is "+longest)