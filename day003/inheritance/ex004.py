# operation

class parent:
    lastName = "park"

    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, where):
        print("{}, trip to {}".format(self.fullName, where))

    def love(self, other):
        print("{} love with {} ".format(self.fullName, other))

    def __add__(self, other):
        print("{} married {}".format(self.fullName, other))

class children(parent):
    lastName = "lee"

    def travel(self, where, day):
        print("{}, trip to {} in {} days".format(self.fullName, where, day))

myParent = parent("ha song")

myChildren = children("chul yeon")

myParent.love("ted")
myParent + myChildren.lastName