def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
d=a+b+c
print("addtion of all values:",d,end=" ")

def hello(name):
    print("hello",name)
name = input("\n enter the name:")
hello(name)

def names(first_name,last_name):
     print("Hello ,my name is:",first_name,last_name)
first_name=input()
last_name=input()
names(first_name,last_name)
#Mixing positional and keyword arguments
def adding(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)
adding(1,2,3)
#models
adding(a=10,b=0,c=1)
adding(3,b=9,c=0)

