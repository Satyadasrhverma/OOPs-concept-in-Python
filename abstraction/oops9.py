from abc import ABC, abstractmethod

class Operation(ABC):
    def __init__(self,a, b):
        self.a = a
        self.b = b
        
    @abstractmethod
    def calculate(self):
        pass

class Sub(Operation):
    def __init__(self, a, b):
        super().__init__(a,b)

    def calculate(self):
        return self.a - self.b

obj = Sub(5,5)
print(obj.calculate())        
     

