class Jam:
	a=1
	b=2
	c=3
	d=a+b+c
	def fun(x):
		print(x.d)
o1=Jam()
o2=Jam()
o3=Jam()
print(o1)
print(o2)
print(o3)
print(o1.a+o1.c)
o1.c=(o1.d)-(o1.b)
print(o1.c)
o2.a=o1.c
print(o1.a,o1.b,o1.c,o1.d,o2.a,o2.b,o2.c,o2.d,
	o3.a,o3.b,o3.c,o3.d,"=",o1.a+o1.b+o1.c+o1.d+
	o2.a+o2.b+o2.c+o2.d+o3.a+o3.b+o3.c+o3.d)
o3.fun()