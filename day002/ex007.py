# 가변인자

def f(args1, args2, args3, *args4):
    print("args is {}".format(args1))
    print("args is {}".format(args2))
    print("args is {}".format(args3))
    print("args is {}".format(args4))

f(1,2,3,4,5,6,7,7,78,78,7,845643)