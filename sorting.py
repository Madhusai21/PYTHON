# Bubble Sort
my_list =[]
num=int(input(" enter the of elements you want:"))
for i in range(num):
    val=int(input("enter the number:"))
    my_list.append(val)
print("given elements ",my_list,end=" ")
for i in range(len(my_list)-1):
    if my_list[i] > my_list[i+1]:
        my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
print("sorted elemnts:",my_list,end=" ")
