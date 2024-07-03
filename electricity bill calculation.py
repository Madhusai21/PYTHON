#write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria
#unit                           price
#first 100 units             no charge
#next 100 units             rs 5 per unit
#after 200 units            rs 10 per unit
amount=0
n=int(input("enter number of electric unit:"))
if n<=100:
    amount=0
if n>100 and n<=200:
    amount=(n-100)*5
if n>200:
    amount=1250+(n-200)*5
    print("amount to pay:",amount)
    
      
      
