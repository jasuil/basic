#deco

import datetime as dt

# def mainfunc():
#     print(dt.datetime.now())
#     print('it\'s main')
#
# def mainfunc2():
#     print(dt.datetime.now())
#     print('it\'s main2')
#
# def mainfunc3():
#     print(dt.datetime.now())
#     print('it\'s main3')
#
# mainfunc()
# mainfunc2()
# mainfunc3()

def datetime_decorator(func):

    def deco():
        print(dt.datetime.now())
        func()
    return deco

@datetime_decorator
def mainfunc():
    print('main func')

@datetime_decorator
def mainfunc2():
    print('main func2')

mainfunc()
mainfunc2()