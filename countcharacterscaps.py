alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msg=input("Enter a message: ")
x=0
while x<len(msg):
	alpha[ord(msg[x])-65]+=1
	x+=1
x=0
while x<len(alpha):
	if alpha[x]!=0:
		print(chr(x+65),"=",alpha[x])
	x+=1