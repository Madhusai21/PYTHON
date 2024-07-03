#capitalize()
m="gopika"
print(m.capitalize())


#center()
print('['+'jaagruthi'.center(20)+']')
print('['+'i love you '.center(50,'*')+']')


#find()
mm="jaagruthi"
print(mm.find("a"))
print(mm.find("agruthi"))
print(mm.find("jaa"))
print(mm.find("amlpouytg"))
print(mm.find("ruthi"))
#example 2
text=" There is also a three-parameter mutation of the find() method – the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search)."
fnd=text.find('the')
while fnd!=-1:
    print(fnd)
    fnd=text.find('the',fnd+1)

    
#endswith
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
#exmaple2
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))


