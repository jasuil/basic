# extension

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("bark")

class Duck(Animal):
    def speak(self):
        print("quack")


#execute
animal = [Dog("hot dog"), Duck("donald")]

for element in animal:
    element.speak()

animal[0].speak()
