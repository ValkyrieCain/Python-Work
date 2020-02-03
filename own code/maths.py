print("Do some addition in your head!")
one=int(input("First number to add: "))
two=int(input("Second number to add: "))
answer=int(input("What's the answer? "))
points=0
if (one+two)==answer:
	print("You got it right!")
	points+=1
else:
	print("That's not correct.")
import time
time.sleep(1)
print("Now for some multiplication!")
one=int(input("First number to multiply: "))
two=int(input("Second number to multiply: "))
answer=int(input("What's the answer? "))
if (one*two)==answer:
	print("You got it right!")
	points+=1
else:
	print("That's not correct.")
time.sleep(1)
print("A bit of division maybe?")
one=int(input("First number to divide: "))
two=int(input("Second number to divide by: "))
answer=int(input("What's the answer? "))
if (one/two)==answer:
	print("You got it right!")
	points+=1
else:
	print("That's not correct.")
time.sleep(1)
print("And finally subtraction.")
one=int(input("First number to subtract from: "))
two=int(input("Second number to subtract: "))
answer=int(input("What's the answer? "))
if (one-two)==answer:
	print("You got it right!")
	points+=1
else:
	print("That's not correct.")
time.sleep(0.5)
print("You got",points,"correct.")