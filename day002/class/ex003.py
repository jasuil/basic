# 문제 3: 사칙연산을 각는  class

class Calc:

    num = 0

    def plus(self, a):
        self.num += a

    def sub(self, a):
        self.num -= a

    def div(self, a):
        self.num /= a

    def mul(self, a):
        self.num *= a


c = Calc()

c.plus(10)
print("10 plus", c.num)

c.mul(2)
print("2 mulitiple ", c.num)

c.sub(10)
print('10 minus ', c.num)

c.div(2)
print('2 divide ', c.num)