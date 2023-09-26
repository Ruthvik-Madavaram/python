class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        return f"{self.name} meows"

dog  = Dog("Scooby", "Golden Retriever")
cat = Cat("Pepper", "Black")

print(f"{dog.name} is a {dog.species} of breed {dog.breed}.", dog.speak())
print(f"{cat.name} is a {cat.species} with {cat.color} fur.", cat.speak())


#Multiple Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
