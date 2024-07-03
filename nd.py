
# IN WE CAN ADD ONE BY ONE LIKE 0+1=1,1+2=3,3+2=5 LIKE IS....////
lst1=int(input())
lst=[]
for i in range(lst1):
    i=int(input())
    lst.append(i)
add=0
lst2=[]
for number in lst:
    add+=number
    lst2.append(add)
print("\n added numbers through the given list:",lst2,end=" ")
n1=[]
n2=[]
for i in lst2:
    if i%2==0:
        n1.append(i)
    else:
        n2.append(i)
print("\n even numbers:",n1,end=" ")
print("\n odd numbers:",n2,end=" ")
mm=min(lst2)
mmm=max(lst2)
print("\n min number of given list:",mm,end=" ")
print("\n max number of given list:",mmm,end=" ")
        



