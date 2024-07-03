num=int(input("enter the price of bike:"))
tax=0
if num>100000:
        tax=15/100*num
elif num >50000 and num<=100000:
        tax=10/100*num
else:
        tax=5/100*num
print("tax to be paid",tax)
        
        
