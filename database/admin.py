import pymysql as sql
data1=sql.connect("localhost","root","","valkyrie")
cur=data1.cursor()
class admin:
	def menu(self):
		self.lines()
		print("Main Menu:")
		print("1 = Enter a new record")
		print("2 = Delete a record")
		print("3 = View a record")
		print("4 = Update a record")
		print("5 = Exit")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			self.create()
		elif interact==2:
			self.delete()
		elif interact==3:
			self.view()
		elif interact==4:
			self.update()
		elif interact==5:
			exit()
		elif interact==6:
			self.secretmenu()
		else:
			print("That's not an option.")
			self.menu()
	def create(self):
		regno=input("Registration Number: ")
		if len(self.unique(regno))!=0:
			print("Registration Number already in use. Please select another number.")
			self.create()
			print((self.unique(regno)))
		else:
			print
			name=input("Name: ")
			codegroup=input("Group: ")
			client=input("Client: ")
			marks=input("Marks: ")
			save=input("Save record? (Y/N) ")
			if "Y" in save.upper():
				cur.execute("insert into consultants values("+regno+",'"+name.upper()+"','"+codegroup.upper()+"','"+client.upper()+"',"+marks+")")
				data1.commit()
				print("Saved!")
			else:
				print("Data discarded.")
			self.menu()
	def view(self):
		self.lines()
		print("Options:")
		print("1 = Show all records")
		print("2 = Show all records with a specific registration number")
		print("3 = Show all records with a specific name")
		print("4 = Show all records from a specific group")
		print("5 = Show all records from a specific client")
		print("6 = Show all records with specific marks")
		print("7 = Go back")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			cur.execute("select * from consultants")
			self.show()
			self.showagain()
		if interact==2:
			regno=input("Which registration number would you like to see? ")
			cur.execute("select * from consultants where regno="+regno)
			self.show()
			self.showagain()
		if interact==3:
			name=input("What name would you like to see? ")
			cur.execute("select * from consultants where name='"+name.upper()+"'")
			self.show()
			self.showagain()
		if interact==4:
			codegroup=input("Which group would you like to see? ")
			cur.execute("select * from consultants where codegroup='"+codegroup.upper()+"'")
			self.show()
			self.showagain()
		if interact==5:
			client=input("Which client would you like to see? ")
			cur.execute("select * from consultants where client='"+client.upper()+"'")
			self.show()
			self.showagain()
		if interact==6:
			marks=input("What marks would you like to see? ")
			cur.execute("select * from consultants where marks="+marks)
			self.show()
			self.showagain()
		if interact==7:
			self.menu()
		else:
			print("That's not an option.")
			self.view()
	def show(self):
		selection=cur.fetchall()
		for file in selection:
			self.lines()
			print("Registration Number:",file[0])
			print("Name:",file[1])
			print("Group:",file[2])
			print("Client:",file[3])
			print("Marks:",file[4])
	def showagain(self):
		self.lines()
		select=input("Would you like to see another record? (Y/N) ")
		if select.upper()=="Y":
			self.view()
		else:
			self.menu()
	def unique(self,x):
		cur.execute("select regno from consultants where regno="+x)
		selection=cur.fetchall()
		return selection
	def lines(self):
		print("--------------------------------------------")
	def secretmenu(self):
		self.lines()
		print("Secret Menu:")
		print("1 = Show hidden records")
		print("2 = Delete all records")
		print("3 = Crash system")
		self.lines()
		interact=int(input("Please select an option: "))
		self.lines()
		if interact==1:
			#put something funny here?
			print("Registration Number: ")
			print("Name: ")
			print("Group: ")
			print("Client: ")
			print("Marks: ")
			self.menu()
		if interact==2:			
			print("All records deleted.")
			exit()
		if interact==3:
			codes=input("Please enter nuclear detonation codes: ")
			print("Processing...")
			time.sleep(3)
			#os.system('shutdown -s')
			#could also make the cmd window close
			#or make the computer bluescreen
		else:
			self.menu()
	def delete(self):
		regno=input("Enter registration number to delete: ")
		cur.execute("select * from consultants where regno="+regno)
		self.show()
		self.lines()
		sure=input("Are you sure you want to delete this record? (Y/N) ")
		if sure.upper()=="Y":
			cur.execute("delete from consultants where regno="+regno)
			data1.commit()
			print("Record deleted.")
		else:
			print("Changes discarded.")
		self.menu()
	def updateagain(self):
		data1.commit()
		print("Changes saved.")
		again=input("Would you like to make another change? (Y/N) ")
		if again.upper()=="Y":
			self.update()
		else:
			self.menu()
	def update(self):
		regno=input("Enter registration number to update: ")
		cur.execute("select * from consultants where regno="+regno)
		self.show()
		self.lines()
		print("1 = Registration Number")
		print("2 = Name")
		print("3 = Group")
		print("4 = Client")
		print("5 = Marks")
		self.lines()
		field=int(input("What field would you like to change? "))
		change=input("What would you like to change the field to? ")
		sure=input("Are you sure you would like to change the field? (Y/N) ")
		if sure.upper()=="Y":
			if field==1:
				cur.execute("update consultants set regno='"+change.upper()+"' where regno="+regno)
			elif field==2:
				cur.execute("update consultants set name='"+change.upper()+"' where regno="+regno)
			elif field==3:
				cur.execute("update consultants set codegroup='"+change.upper()+"' where regno="+regno)
			elif field==4:
				cur.execute("update consultants set client='"+change.upper()+"' where regno="+regno)
			elif field==5:
				cur.execute("update consultants set marks='"+change.upper()+"' where regno="+regno)
			self.updateagain()
		else:
			print("Changes discarded.")
			self.menu()