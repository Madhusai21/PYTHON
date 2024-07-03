def even_numbers(n):
    num=[]
    num1=[]
    for i in range(n):
        if i%2==0:
            num.append(i)
    return num
    for i in range(n):
        if i%3==0:
            num1.append(i)
    return num1
print(even_numbers(11))
            
