import pymysql as sql
import time
import sys
data1=sql.connect("localhost","root","","myfirstdatabase")
class heroes:
	def menu(self):
		self.lines()
		print("Main Menu:")
		print("1 = View heroes")
		print("2 = Enter a new hero")
		print("3 = Update a hero")
		print("4 = Delete a hero")
		print("5 = Exit")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			self.view()
		elif interact==2:
			self.create()
		elif interact==3:
			self.update()
		elif interact==4:
			self.delete()
		elif interact==5:
			exit()
		else:
			print("That's not an option.")
			self.menu()
	def show(self):
		selection=cur.fetchall()
		for file in selection:
			self.lines()
			print("ID No:",file[0])
			print("Publisher:",file[1])
			print("Name:",file[2])
			print("Alter Ego:",file[3])
			print("Powers:",file[4])
			print("Team:",file[5])
			print("Sidekick:",file[6])
			print("Nemesis:",file[7])
			
	def create(self):
		no=input("ID No: ")
		if len(self.unique(no))!=0:
			print("ID No already in use. Please select another number.")
			self.create()
			print((self.unique(no)))
		else:
			print
			publisher=input("Publisher: ")
			name=input("Name: ")
			alterego=input("Alter Ego: ")
			p1=input("Powers: ")
			p2=input("Powers: ")
			p3=input("Powers: ")
			team=input("Team: ")
			sidekick=input("Sidekick: ")
			nemesis=input("Nemesis: ")
			save=input("Save hero? (Y/N) ")
			if "Y" in save.upper():
				cur.execute("insert into superheroes values('publisher.upper()','name.upper()','alterego.upper()','p1.upper()','p2.upper()','p3.upper()','team.upper()','sidekick.upper()','nemesis.upper()'")
				data1.commit()
				print("Saved!")
			else:
				print("Data discarded.")
			self.menu()
	def view(self):
		self.lines()
		print("Options:")
		print("1 = Show all heroes")
		print("2 = Search by publisher")
		print("3 = Search by name")
		print("4 = Search by alter ego")
		print("5 = Search by powers")
		print("6 = Search by team")
		print("7 = Search by sidekick")
		print("8 = Search by nemesis")
		print("9 = Go back")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			cur.execute("select * from superheroes")
			self.show()
			self.showagain()
		if interact==2:
			publisher=input("Publisher: ")
			cur.execute("select * from superheroes where publisher={publisher.upper()}")
			self.show()
			self.showagain()
		if interact==3:
			name=input("Name: ")
			cur.execute("select * from superheroes where name='"+name.upper()+"'")
			self.show()
			self.showagain()
		if interact==4:
			name=input("Alter Ego: ")
			cur.execute("select * from superheroes where alterego='"+alterego.upper()+"'")
			self.show()
			self.showagain()
		if interact==5:
			powers=input("Power: ")
			cur.execute("select * from superheroes where power='"+powers.upper()+"'")
			self.show()
			self.showagain()
		if interact==6:
			client=input("Team: ")
			cur.execute("select * from superheroes where team='"+client.upper()+"'")
			self.show()
			self.showagain()
		if interact==7:
			marks=input("Sidekick: ")
			cur.execute("select * from superheroes where sidekick="+marks)
			self.show()
			self.showagain()
		if interact==8:
			marks=input("Nemesis: ")
			cur.execute("select * from superheroes where nemesis="+marks)
			self.show()
			self.showagain()
		if interact==9:
			self.menu()
		else:
			print("That's not an option.")
			self.view()
	def showagain(self):
		self.lines()
		select=input("Would you like to search again? (Y/N) ")
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
		name=input("Enter hero name to delete: ")
		cur.execute("select * from superheroes where name="+name)
		self.show()
		self.lines()
		sure=input("Are you sure you want to delete this hero? (Y/N) ")
		if sure.upper()=="Y":
			cur.execute("delete from superheroes where name="+name)
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
		no=input("Enter hero name to update: ")
		cur.execute("select * from superheroes where name="+name)
		self.show()
		self.lines()
		print("1 = Publisher")
		print("2 = Name")
		print("3 = Alter Ego:")
		print("4 = Powers")
		print("5 = Team")
		print("6 = Sidekick")
		print("7 = Nemesis")
		self.lines()
		field=int(input("What field would you like to change? "))
		change=input("What would you like to change the field to? ")
		sure=input("Are you sure you would like to change the field? (Y/N) ")
		if sure.upper()=="Y":
			if field==1:
				cur.execute("update superheroes set publisher='"+change.upper()+"' where no="+no)
			elif field==2:
				cur.execute("update superheroes set name='"+change.upper()+"' where no="+no)
			elif field==3:
				cur.execute("update superheroes set alterego='"+change.upper()+"' where no="+no)
			elif field==4:
				cur.execute("update superheroes set powers='"+change.upper()+"' where no="+no)
			elif field==5:
				cur.execute("update superheroes set team='"+change.upper()+"' where no="+no)
			elif field==6:
				cur.execute("update superheroes set sidekick='"+change.upper()+"' where no="+no)
			elif field==7:
				cur.execute("update superheroes set nemesis='"+change.upper()+"' where no="+no)
			self.updateagain()
		else:
			print("Changes discarded.")
			self.menu()
super=heroes()
super.menu()