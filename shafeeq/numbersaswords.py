one=["One","Two","Three","Four","Five","Six","Seven",
"Eight","Nine"]
ten=["Twenty","Thirty","Fourty","Fifty","Sixty",
"Seventy","Eighty","Ninety"]
teen=["Ten","Eleven","Twelve","Thirteen","Fourteen",
"Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
def ones(x):
	if x==0:
		return ""
	else:
		return one[x-1]
def tens(x):
	if x==0:
		return""
	else:
		return ten[x-2]
def teens(x):
	return teen[x]
def hundreds(x):
	if x==0:
		return""
	else:
		return one[x-1]+" Hundred"
def thousands(x):
	if x==0:
		return""
	else:
		return one[x-1]+" Thousand"
number=int(input("Please enter any number: "))
length=len(str(number))
answer=""
def answerones():
	global answer
	answer=answer+ones(number%10)+" "
def answertens(x):
	global answer
	answer=answer+tens(x)+" "
def answerteens(x):
	global answer
	answer=answer+teens(x)+" "
def answerhundreds(x):
	global answer
	answer+=hundreds(x)+" and "
def answerthousands(x):
	global answer
	answer+=thousands(x)+" "
def numberones():
	return number%10
if length==1:
	if number==0:
		print("Zero")
	else:
		print(ones(number))
if length==2:
	t=int(number/10)
	if t==1:
		answerteens(numberones())
	else:
		answertens(t)
		answerones()
	print(answer)
if length==3:
	t=int(number/10)%10
	if t==0 and numberones()==0:
		answer+=hundreds(int(number/100))
	else:
		answerhundreds(int(number/100))
	if t==1:
		answerteens(numberones())
	else:
		answertens(t)
	answerones()
	print(answer)
if length==4:
	t=(int(number/10))%10
	if t==0 and numberones()==0:
		answer+=thousands(int(number/1000))+" "
	else:
		answerthousands(int(number/1000))
	if t==0 and numberones()==0:
		answer+=hundreds((int(number/100))%10)
	else:
		answerhundreds((int(number/100))%10)
	if t==1:
		answerteens(numberones())
	else:
		answertens(t)
	answerones()
	print(answer)