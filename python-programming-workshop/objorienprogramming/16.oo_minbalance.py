
class BankAccount:
    def __init__(self):
        self.balance = 10000

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

a = BankAccount()
b = BankAccount()
c = MinimumBalanceAccount(10000)
d = MinimumBalanceAccount(10000)
print(b.withdraw(1000))
print(a.withdraw(2000))
print(c.deposit(4000))
print(c.withdraw(5000))
print(d.deposit(4000))
print(d.withdraw(5000))
