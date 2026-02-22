class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def show(self):
        return (f"Your Name:", self.name) 
    
p1 = Child("utkarsh")
print(p1.show())    

#--------------------------------------------------------
from abc import ABC , abstractmethod
class Parent:

    def __init__(self, name):
        self.name = name
    @abstractmethod
    def show(self):
        pass

class child(Parent):
    def show(self):
        return f"your name",{self.name} 


c = child("ut")
print(c.show())
