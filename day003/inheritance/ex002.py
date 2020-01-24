# extetion

class houseP:
    lastName = "park"

    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, where):
        print("{}, trip to {}".format(self.fullName, where))


class houseL(houseP):
    lastName = "lee"

    #method overriding
    def travel(self, where, day):
        print("{}, trip to {} in {} days".format(self.fullName, where, day))

mySub = houseL(" java")
mySub.travel("korea", 3)

