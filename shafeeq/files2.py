f=open("elements2.txt","w")
x=1
while x<6:
	name=input("Enter element name: ")
	print(name,file=f)
	x+=1
f=open("elements2.txt")
print(f.readline())
f.readline()
f.readline()
print(f.readline())