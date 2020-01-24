# multi extension

class persionOne:
    def __init__(self):
        self.one = 1

class personTwo:
    def __init__(self):
        self.two = 2

class child(persionOne, personTwo):
    def __add__(self, one, two, three):
        personTwo.__init__(self, one)
        persionOne.__init__(self, two)
        self.three = 3

    #def __init__(self):
        #super().__init__() ##다중 상속에서 부모(super) 호출하는 경우 기재된 순서데로 호출
        #personTwo.__init__(self)
        #persionOne.__init__(self)
        #self.three = 3



#children = child()
children = child(1,2,3)
print(children.__dict__)