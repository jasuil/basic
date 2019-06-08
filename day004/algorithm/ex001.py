# list comprehesion

# catching fruit include character 'a'
fruilts = ['apple', 'banana', 'melon', 'kiwi', 'cherry']
myFruit = [fruit.upper() for fruit in fruilts if 'a' in fruit]
print(myFruit)

# getting odd in 50
b = [x for x in range(1, 51) if x % 2 ==1]
print(b)


print(list(map(lambda x: x**x, [1, 2, 3, 4, 5])))


#examination

eList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
if element x<5 then print x*2
'''
rList = [element * 2 for element in eList if element < 5]
'''
if print x<5 else print x*2
'''
rList2 = [element if element > 5 else element * 2 for element in eList]
print(rList)
print(rList2)

