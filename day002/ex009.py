# fuction

def sample(a, *args, **kwargs):
    print("a is {}".format(a))
    print("args is {}".format(args))
    print("kwargs is {}".format(kwargs)) #파라미터형을 같이 보낼 수 있다.
    print(type(kwargs))


sample(1, 2, 3, 4, name ='jasuil', val = 1212)

