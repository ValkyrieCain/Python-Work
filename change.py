bill=int(input("Enter bill: "))
paid=int(input("Amount paid: "))
change=paid-bill
if paid<bill:
	print("Customer underpaid.")
else:
	if change>=50:
		fifty=int(change/50)
		change=change%50
		print("£50:",fifty)
	else:
		fifty=0
	if change>=20:
		twenty=int(change/20)
		change=change%20
		print("£20:",twenty)
	else:
		twenty=0
	if change>=10:
		ten=int(change/10)
		change=change%10
		print("£10:",ten)
	else:
		ten=0
	if change>=5:
		five=int(change/5)
		change=change%5
		print("£5:",five)
	else:
		five=0
	if change>=2:
		two=int(change/2)
		change=change%2
		print("£2:",two)
	else:
		two=0
	if change>=1:
		one=int(change/1)
		print("£1:",one)
	else:
		one=0
	totalchange=fifty*50+twenty*20+ten*10+five*5+two*2+one
	print("Total change:",totalchange)