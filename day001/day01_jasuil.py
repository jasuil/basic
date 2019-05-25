#for loop

sum = 0
for i in range(11):
    print(i)
    sum += i
print(sum)

myList = ['jasuil', 1212, 'jsi', 12, '성일짱']
for e in myList:
    print(e)


# multiplication table
d = int(input("구구단용 수를 입력 "))

for i in range(1,10):
    print("{} * {} = {}".format(i, d, d * i))


m