my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
print(my_tuple[-1:1])
for elem in my_tuple:
    print(elem)
tuples=(1,10,100)
t1=tuples+(1000,10000)
t2=tuples*3
print(len(t2))
print(t1)
print(t2)
dictonary={"madhu":"sai","jaagruthi":"beauty"}
words={'sai','beauty','gopika'}
for word in words:
    if word in dictonary:
        print(word,"-->",dictonary[word])
    else:
        print(word,"it is not in dict")
