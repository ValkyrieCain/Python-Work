f=open("elements2.txt")
f.readline()
keep=f.readline()+f.readline()+f.readline()+f.readline()
add="This is a new line"
g=open("elements2.txt","w")
print(add,keep,sep="\n",file=g)