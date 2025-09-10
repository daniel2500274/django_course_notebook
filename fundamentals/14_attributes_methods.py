class Person:
    specie = "Human" #class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100
        self.__password= "123."
    def work(self):
        return f"{self.name} is working"
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    def __generate_pasword(self):
        return f"$${self.name}{self.age}$$"


person1 = Person("Daniel", 18) #Instance attribute
print(person1.work())
print(person1._waste_energy(5))