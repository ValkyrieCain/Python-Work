def ones(x):
    if x==1:
        return("One")
    if x==2:
        return("Two")
    if x==3:
        return("Three")
    if x==4:
        return("Four")
    if x==5:
        return("Five")
    if x==6:
        return("Six")
    if x==7:
        return("Seven")
    if x==8:
        return("Eight")
    if x==9:
        return("Nine")
    if x==0:
        return("")
def tens(x):
    if x==2:
        return("Twenty")
    if x==3:
        return("Thirty")
    if x==4:
        return("Fourty")
    if x==5:
        return("Fifty")
    if x==6:
        return("Sixty")
    if x==7:
        return("Seventy")
    if x==8:
        return("Eighty")
    if x==9:
        return("Ninety")
    if x==0:
        return("")
def teens(x):
    if x==1:
        return("Eleven")
    if x==2:
        return("Twelve")
    if x==3:
        return("Thirteen")
    if x==4:
        return("Fourteen")
    if x==5:
        return("Fifteen")
    if x==6:
        return("Sixteen")
    if x==7:
        return("Seventeen")
    if x==8:
        return("Eighteen")
    if x==9:
        return("Nineteen")
    if x==0:
        return("Ten")
number=int(input("Please enter any number: "))
length=len(str(number))
answer=""
def answerones():
	global answer
	answer=answer+ones(number%10)
	#takes the ones digit and returns O
def answertens(x):
	global answer
	answer=answer+tens(x)
    #takes the tens digit and returns Twenty-Ninety
def answerteens(x):
	global answer
    answer=answer+teens(x)
    #takes the ones digit and returns Eleven-Nineteen
def numberones():
    return number%10
def numbertens():
    return int(number/10)
def checkteens():
    if numbertens()==1:
    	#checks if the tens digit is 1
        answerteens(numberones())
    else:
        answertens(numbertens())
if length==1:
    if number==0:
        print("Zero")
    else:
        print(ones(number))
if length==2:
    checkteens()
    answerones()
    print(answer)