
#두 list가 같은지 비교하는 함수


def crit(a,b):

    aSet = set(a)
    bSet = set(b)

    flag = False
    countFalse = 0

    for i in aSet:
        for i2 in bSet:
            if i == i2:
                pass
            else:
                countFalse += 1

    if len(aSet) == len(bSet) and countFalse == 0:
        flag = True


    return flag


print(crit([1,2,3,2,5,6], [1,2,3,2,5,6]))

