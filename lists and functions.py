def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s
print(list_sum([2,3,4]))

#output: 9

#  single integer value mustn't be iterated through by the for loop.
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
 # ouput: [4,3,2,1,0]




