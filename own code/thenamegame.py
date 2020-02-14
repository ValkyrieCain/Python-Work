name = input ("What is your name? ")
name2 = name
vowels = "aeiouAEIOU"

if name2[0] in vowels:
	name2 = name
else:
	name2 = name2.replace(name2[0],"")

if name[0]=="B"or name[0]=="b":
	print (name+"!\n"+name+" "+name+" Bo "+ name2 +
	"\nBanana Fanna Fo F" + name2 + "\nFe Fi Mo M" + name2 + "\n" + name)

elif name[0]=="F" or name[0]=="f":
	print (name + "!\n" + name + " " + name + " Bo " + "B" + name2 +
	"\nBanana Fanna Fo " + name2 + "\nFe Fi Mo M" + name2 + "\n" + name)

elif name[0]=="M" or name[0]=="m":
	print (name + "!\n" + name + " " + name + " Bo " + "B" + name2 +
	"\nBanana Fanna Fo F" + name2 + "\nFe Fi Mo " + name2 + "\n" + name)

else:
	print (name + "!\n" + name + " " + name + " Bo " + "B" + name2 +
	"\nBanana Fanna Fo F" + name2 + "\nFe Fi Mo M" + name2 + "\n" + name)