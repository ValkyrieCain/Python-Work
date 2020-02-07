import random
from add import add
from mult import mult
def test_add():
	i=0
	while i<=100:
		a=random.randint(1,100)
		b=random.randint(1,100)
		assert add(a,b)==(a+b)
		print ("True")
		i+=1
def test_mult():
	i=0
	while i<=100:
		a=random.randint(1,100)
		b=random.randint(1,100)
		assert mult(a,b)==(a*b)
		print ("True")
		i+=1