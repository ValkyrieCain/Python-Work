class functions:
	def createfile(self):
		filename=input("What file would you like to create? ")+".txt"
		file=open(filename,"a")
	def insertrecords(self):
		filename=input("Which file would you like to edit? ")+".txt"
		file=open(filename,"a")
		print(input("What would you like to insert? "),file=file)
	def find(self):
		filename=input("Which file would you like to search? ")+".txt"
		file=open(filename,"r")
		findword=input("String to look for: ")
		position=0
		counter=0
		for line in file:
			for i in line:
				if i==findword[0]:
					if line[position:position+len(findword)]==findword:
						counter+=1
				position+=1
			position=0
		if counter==1:
			print("The string",findword,"appeared",counter,"time.")
		else:
			print("The string",findword,"appeared",counter,"times.")
	def findandreplace (self):
		filename=input("Which file would you like to search? ")+".txt"
		fileread=open(filename,"r")
		findword=input("String to look for: ")
		replaceword=input("String to replace with: ")
		replaceline=""
		position=0
		counter=0
		for line in fileread:
			while position<len(line):
				if line[position:position+len(findword)]==findword:
					replaceline+=replaceword
					counter+=1
					position+=len(findword)-1
				else:
					replaceline+=line[position]
				position+=1
			position=0
		filewrite=open(filename,"w")
		print(replaceline,file=filewrite)
		print("Replacements made:",counter)
user=functions()
repeat=True
while repeat==True:
	print("------------------------------")
	print("Functions:")
	print("1 = Create a blank file")
	print("2 = Insert into a file")
	print("3 = Find in a file")
	print("4 = Find and replace in a file")
	print("5 = Exit")
	print("------------------------------")
	interact=int(input(""))
	if interact==1:
		user.createfile()
	if interact==2:
		user.insertrecords()
	if interact==3:
		user.find()
	if interact==4:
		user.findandreplace()
	if interact==5:
		repeat=False