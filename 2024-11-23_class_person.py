class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive number.")

    def get_name(self):
        return self.__name

    def get_age(self):
        if self.__age>0:
            return self.__age

# Creating a person object
person = Person()
person.set_name("rajesh")
person.set_age(25)

print(f"Name: {person.get_name()} \nAge: {person.get_age()}")

