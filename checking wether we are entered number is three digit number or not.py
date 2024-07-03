# write a program to check whether a number entered is three digit number or not
num=input("enter the number:")
l=len(num)
if l==3:
        print("it is a three digit number".format(num))
else:
        print(" it is not a three digit number".format(num))
