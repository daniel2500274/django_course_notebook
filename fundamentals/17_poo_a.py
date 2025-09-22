class BankAccount:
    def __init__(self,owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance #Encapsulation attributes
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Deposit error, amount invalid")
    def check_balance(self):
        return f"Actual balance: {self.__balance}"

account = BankAccount("Daniel", 100) #abstraction
print(account.check_balance())
account.deposit(100)
print(account.check_balance())
account.withdraw(100.95)
print(account.check_balance())