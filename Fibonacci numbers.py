
def fib(n):
    if n<3:
        return 1
    ele1=ele2=1
    the_sum=0
    for i in range (3,n+1):
        the_sum=ele1+ele2
        ele1,ele2=ele2,the_sum
    return the_sum
for n in range(1,10):
    print(n,"-->",fib(n))
    
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
for n in range(1,6):
    print( n,"-->",factorial_function(n))


    
