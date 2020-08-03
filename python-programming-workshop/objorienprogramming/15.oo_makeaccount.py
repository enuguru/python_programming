
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
b = BankAccount()
print(a.deposit(10000))
print(b.deposit(5000))
print(b.withdraw(1000))
print(a.withdraw(1000))
