# function

def f(i, myList):
    i += 1
    myList.append(0)

k = 10 #k는 int(immutable)
m = [1, 2, 3] #m은 list(mutable)

f(k, m)
print(k, m)



#####################
def calc(i, j, factor = 1):
    return i * j * factor

result = calc(10, 20)
print(result)


#####################
def myF(i, myList, j = 'jasuil'):
    i += 1
    myList.append(0)
    jasuil = 'jasuil1212'
    return i, myList

jasuil = 'j'
i=0
i, m = myF(i, m)

print(i, m, jasuil)
