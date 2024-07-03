mylist=[12,3,4,5]
total=0
for i in range(len(mylist)):
    total+=mylist[i]
print("addition of numbers:",total)
/// even and odd numbers
mm=int(input())
n=[]
for i in range(mm):
    i=int(input())
    n.append(i)
n1=[]
n2=[]
for i in(n):
    if i%2==0:
        n1.append(i)
    else:
        n2.append(i)
print("\n even numbers are:",n1,end=" ")
print("\n odd numbers are:",n2,end=" ")

    
