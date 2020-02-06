import pymysql as sql
data1=sql.connect("localhost","root","","myfirstdatabase")
cur=data1.cursor()
file=open("myfirsttable.txt","w")
cur.execute("select * from myfirsttable order by idno asc")
x=cur.fetchall()
for y in x:
	print(y,file=file)
print("myfirsttable.txt successfully updated!")