# abstraction, hierarchy
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance #Encapsulation attributes
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def _get_balance(self):
        return self.__balance
    def _set_balance(self, amount):
        self.__balance = amount
    @abstractmethod
    def withdraw(self, amount): #overrite the functionality of this method, polymorphism
        pass
    def check_balance(self):
        return f"Actual balance: {self.__balance}"

class SavingsAccount(BankAccount): # hierarchy
    def withdraw(self, amount):
        penalty = amount * 0.05
        total = amount + penalty
        if self._get_balance() >= total:
            self._set_balance(self._get_balance()-total)
        else:
            print("You can't withdraw money, because don´t have sufficient funds")

class PayrollAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0:
            self._set_balance(self._get_balance()+amount)
        else:
            print("You can't withdraw money, because don´t have sufficient funds")

savings_account = SavingsAccount("Daniel", 8500)
savings_account.withdraw(100)
print("Savings Acount" + savings_account.check_balance())
checking_account = PayrollAccount("Daniel", 8500)
checking_account.withdraw(100)
print(checking_account.check_balance())