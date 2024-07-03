n=0
num=int(input("enter the numbers:"))
if num==0 and num==1:
     n=1
for i in range (2,num):
    if num%i==0:
       n=1
if n==1:
    print("it is not a prime number") 
else:
    print("it is a prime number")
