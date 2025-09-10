class Person:
    specie = "Human"
    hair = "Curly"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_specie(self, new_specie): # instance level
        self.specie = new_specie
    @classmethod # when classmethod is used, you can modify the class
    def change_hair(cls, new_hair):
        cls.hair = new_hair
    @staticmethod  #you can access this to a class or instance
    def change_age(new_age):
        return new_age>=18

person1 = Person("Daniel", 18)
person2 = Person("Daniel", 19)
print(person1.name)
print(person1.age)
print(person1.specie)
person1.change_specie("Ciborg")
print(person1.name)
print(person1.age)
print(person1.specie)
Person.change_hair("Curly")