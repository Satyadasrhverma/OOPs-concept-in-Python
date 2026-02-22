# ---------------- Parent Class ----------------
class Dog:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Dog Name: {self.name}")


# ---------------- Single Inheritance ----------------
class Labrador(Dog):
    def __init__(self, name):
        super().__init__(name)   # calls Dog.__init__

    def sound(self):
        print("Labrador Dog")


# ---------------- Multilevel Inheritance ----------------
class GuideDog(Labrador):
    def __init__(self, name):
        super().__init__(name)   # goes to Labrador → Dog

    def guide(self):
        print(f"{self.name} guides this way")


# ---------------- Multiple Inheritance ----------------
class Friendly:
    def __init__(self):
        pass

    def greet(self):
        print("Friendly Dog")


class Golden(Dog, Friendly):
    def __init__(self, name):
        super().__init__(name)   # Dog.__init__ is called
        Friendly.__init__(self)  # explicit call (important in multiple inheritance)

    def sound(self):
        print(f"{self.name}Golden Bark")


l = Labrador("Buddy")
l.sound()

g = GuideDog("Max")
g.display()
g.guide()

f = Golden("Charlie")
f.display()
f.greet()
f.sound()
