num = "5"
print(num)
while int(num)<6:
  for i in range(2,int(num)):
    if (int(num) % i) == 0:
      print(int(num),"is not a prime number")
      print(i,"times",int(num)//i,"is",int(num))
      num=(num+"5")
      print(num)
    else:
      print(int(num),"is a prime number")
      num=(num+"5")
      print(num)
else:
  break