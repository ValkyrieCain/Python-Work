one=["","One","Two","Three","Four","Five","Six","Seven",
"Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen",
"Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
ten=["Twenty","Thirty","Fourty","Fifty","Sixty",
"Seventy","Eighty","Ninety"]
def ones(x):
	return one[x]
def tens(x):
	return ten[x-2]
number=int(input("Please enter any number (max 99999): "))
answer=""
if number==0:
	answer+="Zero"
if number>=10000:
	if int(number/10000)==1:
		answer+=ones(int(number/1000))+" Thousand "
		number=number%1000
	elif (int(number/1000))%10==0:
		answer+=tens(int(number/10000))+" Thousand "
	else:
		answer+=tens(int(number/10000))+" "
	number=number%10000
if number>=1000:
	answer+=ones(int(number/1000))+" Thousand "
	number=number%1000
if number>=100:
	answer+=ones(int(number/100))+" Hundred "
	number=number%100
if number!=0:
	if number>=20:
		answer+="and "+tens(int(number/10))+" "
		number=number%10
	if number<=19:
		if " and" in answer:
			answer+=ones(number)
		else:
			answer+="and "+ones(number)	
print(answer)