import pymysql as sql
data1=sql.connect("localhost","root","","valkyrie")
cur=data1.cursor()
class test:
	def inser(self):
		num="55"
		name="rr"
		cur.execute(f"insert into test values({num},'{name}')")
		data1.commit()
tt=test()
tt.inser()