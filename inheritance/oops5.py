class Dog:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Dog:", self.name)


class Labrador(Dog):
    def __init__(self, name, color):
        super().__init__(name)    # parent constructor
        self.color = color

    def display(self):
        super().display()         # parent method
        print("Color:", self.color)


lab = Labrador("Bruno", "Black")
lab.display()
## super or init menthos in child class