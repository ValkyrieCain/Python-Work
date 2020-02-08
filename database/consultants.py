import pymysql as sql
import time
import sys
from guest import guest
from admin import admin
data1=sql.connect("localhost","root","","myfirstdatabase")
cur=data1.cursor()
password=input("Enter admin password: ")
if password=="69":
	admin=admin()
	print("Logging in as admin...")
	time.sleep(2)
	admin.menu()
else:
	guest=guest()
	print("Logging in as guest...")
	time.sleep(2)
	guest.menu()