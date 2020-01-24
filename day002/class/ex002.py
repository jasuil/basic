#class

class Calculator:
    result = 0 #define and set

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = 0

    def plus(self, num):
        self.result = self.x + self.y
        return self.result


call = Calculator(1, 2)
call2 = Calculator(-2, 4.7)

print(call.plus(10))
print(call.plus(-3))

print(call2.plus(12))
print(call is call2)