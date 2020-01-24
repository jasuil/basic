# global args

x = 50

def func():

    global x
    print('x is ', x)

    x=20
    print('changed x is ', x)


func()
print('changed global x is ', x)

