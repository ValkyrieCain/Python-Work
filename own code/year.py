year=1992
leap=False
if year%4!=0:
    leap=False
elif year%4==0:
	if year%100==0:
  	  	if year%400==0:
			leap=True
		else:
			leap=False
print(leap)