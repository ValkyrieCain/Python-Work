year=int(input("Enter a year and find out if it was/will be a leap year (cannot be before 1000AD): "))
leap=False
if year%4==0:
    leap=True
if year%100==0:
	leap=False
if year%400==0:
	leap=True
if year<2020:
	if leap==True:
		print(year,"was a leap year.")
	else:
		print(year,"was not a leap year.")
else:
	if leap==True:
		print(year,"will be a leap year.")
	else:
		print(year,"will not a leap year.")