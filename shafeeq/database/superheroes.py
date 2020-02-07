import pymysql as sql
import time
import sys
data1=sql.connect("localhost","root","","myfirstdatabase")
class heroes:
	def menu(self):
		self.lines()
		print("Main Menu:")
		print("1 = Enter a new hero")
		print("2 = Delete a hero")
		print("3 = View a hero")
		print("4 = Update a hero")
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
		else:
			print("That's not an option.")
			self.menu()
	def show(self):
		selection=cur.fetchall()
		for file in selection:
			self.lines()
			print("Registration Number:",file[0])
			print("Publisher:",file[1])
			print("Name:",file[2])
			print("Powers:",file[3])
			print("Teams:",file[4])
			print("Sidekicks:",file[5])
			print("Nemeses:",file[4])
			
	def create(self):
		no=input("Registration Number: ")
		if len(self.unique(no))!=0:
			print("Registration Number already in use. Please select another number.")
			self.create()
			print((self.unique(no)))
		else:
			print
			name=input("Name: ")
			publisher=input("publisher: ")
			client=input("Client: ")
			marks=input("Marks: ")
			save=input("Save hero? (Y/N) ")
			if "Y" in save.upper():
				cur.execute("insert into superheroes values("+no+",'"+name.upper()+"','"+publisher.upper()+"','"+client.upper()+"',"+marks+")")
				data1.commit()
				print("Saved!")
			else:
				print("Data discarded.")
			self.menu()
	def view(self):
		self.lines()
		print("Options:")
		print("1 = Show all heroes")
		print("2 = Show all heroes with a specific registration number")
		print("3 = Show all heroes with a specific name")
		print("4 = Show all heroes from a specific publisher")
		print("5 = Show all heroes from a specific client")
		print("6 = Show all heroes with specific marks")
		print("7 = Go back")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			cur.execute("select * from superheroes")
			self.show()
			self.showagain()
		if interact==2:
			no=input("Which registration number would you like to see? ")
			cur.execute("select * from superheroes where no="+no)
			self.show()
			self.showagain()
		if interact==3:
			name=input("What name would you like to see? ")
			cur.execute("select * from superheroes where name='"+name.upper()+"'")
			self.show()
			self.showagain()
		if interact==4:
			publisher=input("Which publisher would you like to see? ")
			cur.execute("select * from superheroes where publisher='"+publisher.upper()+"'")
			self.show()
			self.showagain()
		if interact==5:
			client=input("Which client would you like to see? ")
			cur.execute("select * from superheroes where client='"+client.upper()+"'")
			self.show()
			self.showagain()
		if interact==6:
			marks=input("What marks would you like to see? ")
			cur.execute("select * from superheroes where marks="+marks)
			self.show()
			self.showagain()
		if interact==7:
			self.menu()
		else:
			print("That's not an option.")
			self.view()
	def showagain(self):
		self.lines()
		select=input("Would you like to see another hero? (Y/N) ")
		if select.upper()=="Y":
			self.view()
		else:
			self.menu()
	def unique(self,x):
		cur.execute("select no from superheroes where no="+x)
		selection=cur.fetchall()
		return selection
	def lines(self):
		print("--------------------------------------------")
	def delete(self):
		no=input("Enter registration number to delete: ")
		cur.execute("select * from superheroes where no="+no)
		self.show()
		self.lines()
		sure=input("Are you sure you want to delete this hero? (Y/N) ")
		if sure.upper()=="Y":
			cur.execute("delete from superheroes where no="+no)
			data1.commit()
			print("Hero deleted.")
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
		no=input("Enter registration number to update: ")
		cur.execute("select * from superheroes where no="+no)
		self.show()
		self.lines()
		print("1 = Registration Number")
		print("2 = Publisher")
		print("3 = Name")
		print("4 = Client")
		print("5 = Marks")
		self.lines()
		field=int(input("What field would you like to change? "))
		change=input("What would you like to change the field to? ")
		sure=input("Are you sure you would like to change the field? (Y/N) ")
		if sure.upper()=="Y":
			if field==1:
				cur.execute("update superheroes set no='"+change.upper()+"' where no="+no)
			elif field==2:
				cur.execute("update superheroes set name='"+change.upper()+"' where no="+no)
			elif field==3:
				cur.execute("update superheroes set publisher='"+change.upper()+"' where no="+no)
			elif field==4:
				cur.execute("update superheroes set client='"+change.upper()+"' where no="+no)
			elif field==5:
				cur.execute("update superheroes set marks='"+change.upper()+"' where no="+no)
			self.updateagain()
		else:
			print("Changes discarded.")
			self.menu()
super=heroes()
super.menu()