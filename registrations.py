file=open("records.txt","a")
while True:
	regno=input("Enter registration number: ")+","
	name=input("Enter your name: ")+","
	address=input("Enter your address: ")
	save=input("Do you want to save the record? (Y/N) ")
	if save=="n" or save=="N":
		pass
	elif save=="y" or save=="Y":
		print(regno,name,address,file=file)
	else:
		print("Error: please use Y/N.")
	again=input("Do you want to add another record? (Y/N) ")
	if again=="y" or again=="Y":
		pass
	elif again=="n" or again=="N":
		break
	else:
		print("Error: please use Y/N.")
		break