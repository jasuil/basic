# 가변적 인자

def total(*numbers): #tuple형태로 받습니다.

    tot = 0

    for i in numbers:
        tot += i

    return tot


t = total(1, 2)
print(t)

t = total(1, 2, 34, -3, 345)
print(t)