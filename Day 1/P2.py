#Parent class/base class
class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        return "Some Sound"
    
#Child class/derived class
class Cat(Animal):
    def makeSound(self):
        return f"{self.name} says Meow"
    
#Child class/derived class
class Cow(Animal):
    def makeSound(self):
        return f"{self.name} says Moo"

cat =Cat("Tom")
cow = Cow ("Jerry")

print(cat.makeSound())
print(cow.makeSound())