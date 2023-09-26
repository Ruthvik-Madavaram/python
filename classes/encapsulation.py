class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


person = Person("Dhoni", 41)

print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Ruthvik")
person.set_age(23)

person.display_info()
