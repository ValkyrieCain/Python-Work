import pymysql as sql
data1=sql.connect("localhost","root","","valkyrie")
cur=data1.cursor()
class guest:
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
			print("Action not available for guest user.")
			self.menu()
		elif interact==3:
			self.view()
		elif interact==4:
			print("Action not available for guest user.")
			self.menu()
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