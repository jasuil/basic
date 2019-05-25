# s = 'jasuil'
#
# print(s)
#
# print(s[0]) #일부분
#
# print(s[1:2])
#
# print(s[1:])
#
# print(s[:3]) #범위제한
#
# print(s*3) #반복출력



########################
# myList = [1, 'adf', 'jasuil', 4.5, 'sdfdsf']
# mList = [34, 'dsf', 1]
# myList.append('sdf')
# myList.insert(2, ' 성일짱')
# print("my list", myList)
# print(myList[0])
# print("하한 제한" , myList[1:])
# print("상한 제한 " , myList[:3])
# print(mList*2)
# print(myList + mList)

########################



# myTuple = (-1.34, '성일짱', '짱성일', 23)
#
# print(myTuple)
# print("범위제한", myTuple[1:2])
# print("범위제한", myTuple[-3:-2])
# print(myTuple[1:-1])
# print(myTuple \
#       , 1)


#print("jasuil"[3] + 1) type error

########################

#dictionary
# myDict = {}
# myDict['jasuil'] = 'jasuil is a good guy'
# myDict[3] = 1212
#
# myDict2 = {'jsi':'jsio', 23: 2123}
#
# print(myDict)
# print(myDict[3])
# print(myDict2)
# print(myDict2.values())
# print(myDict2.keys())

######################
#set

# myset = {1,2,'jasuil'}
#
# myset.add('jsi')
# print(myset)
#
# myset.remove('jasuil')
# myset.remove(2)
# print(myset)
#
# myset.clear()
# print(myset)
#
# myset = set('asdfsadfsadfsafsa')
# print(myset)

#####################
#set operation

s1 = set([1,2,3,4,5,6,7,8,9])
s2 = set([4,5,6,7,8,9,0])

print("intersection ", s1 & s2)
print("intersection", s2.intersection(s1))
print("union", s1 | s2)
print("difference", s1 - s2)
print("difference", s2.difference(s2))

s1.add(21)
print("add", s1)

