one=["","One","Two","Three","Four","Five","Six","Seven",
"Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen",
"Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
ten=["Twenty","Thirty","Fourty","Fifty","Sixty",
"Seventy","Eighty","Ninety"]
def ones(x):
	return one[x]
def tens(x):
	return ten[x-2]
number=int(input("Please enter any number: "))
answer=""
if number>=1000:
	if (int(number/100))%10==0:
		if number%10==0 or (int(number/10))%10==0:
			answer=ones(int(number/1000))+" Thousand and "
		else:
			answer=ones(int(number/1000))+" Thousand "
	else:
		answer=ones(int(number/1000))+" Thousand "
	number=number%1000
if number>=100:
	if number%100==0:
		answer+=ones(int(number/100))+" Hundred"
	else:
		answer+=ones(int(number/100))+" Hundred and "
	number=number%100
if number>=20:
	answer+=tens(int(number/10))+" "
	number=number%10
if number<=19:
	if number==0:
		answer+="Zero"
	else:
		answer+=ones(number)
print(answer)