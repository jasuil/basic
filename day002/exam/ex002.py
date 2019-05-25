#두 list가 같은지 비교하는 함수

def crit(a,b):

    aSet = set(a)
    bSet = set(b)
    sameLength = False
    sameElement = True

    for e in aSet:
        if e in bSet: pass
        else: sameElement = False

    if len(aSet) == len(bSet): sameLength = True

    return sameLength & sameElement

print(crit([1,2,3], [1,2,3]))
