import pymysql as sql
data1=sql.connect("localhost","root","","myfirstdatabase")
cur=data1.cursor()
file=open("myfirsttable.txt","w")
print(cur.execute("instructions here"),file=file)
print("myfirsttable.txt successfully updated!")