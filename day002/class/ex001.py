#class

class Rectagle:

    count = 0

    #initializer(생성자)
    def __init__(self, width, height):
        #self: instance variance
        self.width = width
        self.height = height
        Rectagle.count += 1

    def calcArea(self):
        area = self.width * self.height
        return area

#make an instance
r = Rectagle(10, 20)

print('Area is ', r.calcArea())