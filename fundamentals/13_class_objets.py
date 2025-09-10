class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        return f"{self.name} is working"

person1 = Person("Daniel", 18)
print(person1.work())