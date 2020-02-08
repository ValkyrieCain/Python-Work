import pymysql as sql
data1=sql.connect("localhost","root","","myfirstdatabase")
cur=data1.cursor()
while True:
	idno=input("Enter ID Number: ")
	name=input("Enter name: ")
	age=input("Enter age: ")
	save=input("Do you want to save the record? (Y/N) ")
	if save=="n" or save=="N":
		pass
	elif save=="y" or save=="Y":
		cur.execute("insert into myfirsttable values("+idno+",'"+name+"',"+age+")")
		data1.commit()
		print("Saved!")
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