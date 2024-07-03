num=int(input("enter the year:"))
if num%100==0:
   if num%400==0:
        print(" enter year is  leap year")
   else:
        print("enter year is not leap year")
else:
    if num%4==0:
        print("enter year is leap year")
    else:
        print("enter year is not leap year")
