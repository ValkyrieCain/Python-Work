class one:
	def m1(self):
		print("Hello")
class two(one):
	def m2(self):
		print("my friends.")
class three(two):
	def m3(self):
		print("world.")
x=three()
x.m1()
x.m3()
class four:
	def m4(self):
		print("Tuesday")
class five(one,four):
	def m5(self):
		print("Friday")
y=five()
y.m1()
y.m4()
y.m5()