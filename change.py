bill=int(input("Enter bill: "))
paid=int(input("Amount paid: "))
change=paid-bill
if change>=50:
	fifty=int(change/50)
	change=change%50
else:
	fifty=0
if change>=20:
	twenty=int(change/20)
	change=change%20
else:
	twenty=0
if change>=10:
	ten=int(change/10)
	change=change%10
else:
	ten=0
if change>=5:
	five=int(change/5)
	change=change%5
else:
	five=0
if change>=2:
	two=int(change/2)
	change=change%2
else:
	two=0
if change>=1:
	one=int(change/1)
else:
	one=0
if fifty!=0:
	print("£50:",fifty)
if twenty!=0:
	print("£20:",twenty)
if ten!=0:
	print("£10:",ten)
if five!=0:
	print("£5:",five)
if two!=0:
	print("£2:",two)
if one!=0:
	print("£1:",one)
totalchange=fifty*50+twenty*20+ten*10+five*5+two*2+one*1
print("Total change:",totalchange)