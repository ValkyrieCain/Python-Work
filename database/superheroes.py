import pymysql as sql
data1=sql.connect("localhost","root","","valkyrie")
cur=data1.cursor()
class heroes:
	def menu(self):
		self.lines()
		print("Main Menu:")
		print("1 = View heroes")
		print("2 = Enter a new hero")
		print("3 = Change a hero")
		print("4 = Delete a hero")
		print("5 = Exit")
		self.lines()
		interact=int(input("Please select an option: "))
		if interact==1:
			self.read()
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
	def create(self):
		publisher=input("Publisher: ")
		name=input("Name: ")
		alterego=input("Alter Ego: ")
		p1=input("First Power: ")
		p2=input("Second Power: ")
		p3=input("Third Power: ")
		team=input("Team: ")
		sidekick=input("Sidekick: ")
		nemesis=input("Nemesis: ")
		save=input("Save hero? (Y/N) ")
		if "Y" in save.upper():
			if len(self.unique(p1))==0:
				cur.execute(f"insert into powers values ({self.max()}+1,'{p1.upper()}')")
			if len(self.unique(p2))==0:					
				cur.execute(f"insert into powers values ({self.max()}+1,'{p2.upper()}')")
			if len(self.unique(p3))==0:
				cur.execute(f"insert into powers values ({self.max()}+1,'{p3.upper()}')")
			cur.execute(f"insert into superheroes values('"+publisher.upper()+"','"+name.upper()+"','"+alterego.upper()+
				"',(select pid from powers where power='"+p1.upper()+"'),(select pid from powers where power='"+p2.upper()+
				"'),(select pid from powers where power='"+p3.upper()+"'),'"+team.upper()+"','"+sidekick.upper()+"','"+nemesis.upper()+"')")
			data1.commit()
			print("Saved!")
		else:
			print("Data discarded.")
		self.menu()
	def read(self):
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
			cur.execute(f"select * from superheroes")
			self.show()
			self.showagain()
		if interact==2:
			publisher=input("Publisher: ")
			cur.execute(f"select * from superheroes where publisher='{publisher.upper()}'")
			self.show()
			self.showagain()
		if interact==3:
			name=input("Name: ")
			cur.execute(f"select * from superheroes where name='{name.upper()}'")
			self.show()
			self.showagain()
		if interact==4:
			alterego=input("Alter Ego: ")
			cur.execute(f"select * from superheroes where alterego='{alterego.upper()}'")
			self.show()
			self.showagain()
		if interact==5:
			powers=input("Power: ")
			cur.execute(f"select * from superheroes where power1=(select pid from powers where power1='"+powers.upper()+
				"') or power2=(select pid from powers where power='"+powers.upper()+
				"') or power3=(select pid from powers where power='"+powers.upper()+"')")
			self.show()
			self.showagain()
		if interact==6:
			team=input("Team: ")
			cur.execute(f"select * from superheroes where team='{team.upper()}'")
			self.show()
			self.showagain()
		if interact==7:
			sidekick=input("Sidekick: ")
			cur.execute(f"select * from superheroes where sidekick='{sidekick.upper()}'")
			self.show()
			self.showagain()
		if interact==8:
			nemesis=input("Nemesis: ")
			cur.execute(f"select * from superheroes where nemesis='{nemesis.upper()}'")
			self.show()
			self.showagain()
		if interact==9:
			self.menu()
		else:
			print("That's not an option.")
			self.read()
	def update(self):
		self.lines()
		name=input("Enter the alter ego of the hero you would like to change: ")
		cur.execute(f"select * from superheroes where alterego='{name}'")
		self.show()
		self.lines()
		print("1 = Publisher")
		print("2 = Name")
		print("3 = Alter Ego")
		print("4 = First Power")
		print("5 = Second Power")
		print("6 = Third Power")
		print("7 = Team")
		print("8 = Sidekick")
		print("9 = Nemesis")
		print("10 = Go back")
		self.lines()
		field=int(input("What field would you like to change? "))
		if field==10:
			self.menu()
		change=input("What would you like to change the field to? ")
		sure=input("Are you sure you would like to change the field? (Y/N) ")
		if sure.upper()=="Y":
			if field==1:
				cur.execute(f"update superheroes set publisher='{change.upper()}' where alterego='{name}'")
			elif field==2:
				cur.execute(f"update superheroes set name='{change.upper()}' where alterego='{name}'")
			elif field==3:
				cur.execute(f"update superheroes set alterego='{change.upper()}' where alterego='{name}'")
			elif field==4:
				if len(self.unique(change))==0:
					cur.execute(f"insert into powers values ({self.max()}+1,'{change.upper()}')")
				cur.execute(f"update superheroes set power1=(select pid from powers where power='{change.upper()}') where alterego='{name}'")
			elif field==5:
				if len(self.unique(change))==0:
					cur.execute(f"insert into powers values ({self.max()}+1,'{change.upper()}')")
				cur.execute(f"update superheroes set power2=(select pid from powers where power='{change.upper()}') where alterego='{name}'")
			elif field==6:
				if len(self.unique(change))==0:
					cur.execute(f"insert into powers values ({self.max()}+1,'{change.upper()}')")
				cur.execute(f"update superheroes set power3=(select pid from powers where power='{change.upper()}') where alterego='{name}'")
			elif field==7:
				cur.execute(f"update superheroes set team='{change.upper()}' where alterego='{name}'")
			elif field==8:
				cur.execute(f"update superheroes set sidekick='{change.upper()}' where alterego='{name}'")
			elif field==9:
				cur.execute(f"update superheroes set nemesis='{change.upper()}' where alterego='{name}'")
			else:
				print("Field incorrectly selected.")
				self.update()
			self.updateagain()
		else:
			print("Changes discarded.")
			self.menu()
	def delete(self):
		name=input("Enter the alter ego of the hero you would like to delete: ")
		cur.execute(f"select * from superheroes where alterego='{name}'")
		self.show()
		self.lines()
		sure=input("Are you sure you want to delete this hero? (Y/N) ")
		if sure.upper()=="Y":
			cur.execute(f"delete from superheroes where alterego='{name}'")
			data1.commit()
			print("Hero deleted.")
		else:
			print("Changes discarded.")
		self.menu()
	def show(self):
		selection=cur.fetchall()
		for file in selection:
			self.lines()
			print("Publisher:",file[0])
			print("Name:",file[1])
			print("Alter Ego:",file[2])
			cur.execute(f"select power from powers where pid={file[3]} or pid={file[4]} or pid={file[5]}")
			pwr=cur.fetchall()
			for p in pwr:
				print("Powers:",p[0])
			print("Team:",file[6])
			print("Sidekick:",file[7])
			print("Nemesis:",file[8])
	def updateagain(self):
		data1.commit()
		print("Changes saved.")
		again=input("Would you like to make another change? (Y/N) ")
		if again.upper()=="Y":
			self.update()
		else:
			self.menu()
	def showagain(self):
		self.lines()
		select=input("Would you like to search again? (Y/N) ")
		if select.upper()=="Y":
			self.read()
		else:
			self.menu()
	def unique(self,x):
		cur.execute(f"select pid from powers where power='{x}'")
		selection=cur.fetchall()
		return selection
	def max(self):
		cur.execute(f"select max(pid) from powers")
		selection=cur.fetchall()
		for x in selection:
			return x[0]
	def lines(self):
		print("--------------------------------------------")
super=heroes()
super.menu()