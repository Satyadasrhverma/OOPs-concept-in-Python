#Abstraction

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        print("Calculating salary...")


class Developer(Employee):
    def salary(self):
        print("Developer salary: 50k")


class Tester(Employee):
    def salary(self):
        print("Tester salary: 40k")


d = Developer()
d.salary()
