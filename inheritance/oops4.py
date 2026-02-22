class Dog:
    def __init__(self , name):
        self.name = name
    def display(self):
        print(f"Dog Namec: {self.name}")
class Labrador(Dog): # Single Inheritance
    def sound (self):
        print("Labrador Dog")

# Multilevel Inheritance


class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}, Guides this way")


# Multiple Inheritance

class Freindly:
    def greet(self):
        print("Freindly")

class Golden(Dog,Freindly):
    def sound(self):
        print("Bark")

l = Labrador("Buddy")
l.sound()

e = GuideDog("Max")
e.display()

f = Golden("Charlie")
f.greet()

