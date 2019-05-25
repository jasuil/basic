# function

def print_f(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(type(kwargs))

    for name, value in kwargs.items():
        print("{}, {}".format(name, value))

print_f(first = 1, second = 2, third = 'jasuil', fourth = '성일짱')