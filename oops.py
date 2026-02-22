class Dog:
    species = "Felin"

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
dog1 = Dog("Bunny", 3)
dog2 = Dog("sitaa", 4)

print(f"the name of dog ",dog1.name, "and the age of dog is" , dog1.age)
print(f"the name of dog ",dog2.name, "and the age of dog is" , dog2.age)
print(dog1.species)

#update the dog 1 name

dog1.name = "Berlin"

#update the dog speices

Dog.species = "Kelvin"

print(f"the name of dog ",dog1.name, "and the age of dog is" , dog1.species)