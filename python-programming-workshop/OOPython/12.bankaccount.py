
# BankAccount.py - Gururajan Narasimhan modified original program 
# program by written by Jimmy kurian

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        minimum_balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def overdrawn(self):
        return self.balance < 0


class SavingsBankAccount(BankAccount):
    def __init__(self, initial_balance=0):
        BankAccount.__init__(self,initial_balance)
        self.balance = initial_balance
        self.minimum_balance = 5000
    def withdraw(self, amount):
        if((self.balance - amount) < self.minimum_balance):
            print("You do not have minimum balance")
        else:
            self.balance = self.balance - amount
            print(self.balance)


my_account = BankAccount(10000)
my_account.withdraw(500)
my_account.deposit(7000)
print(my_account.balance)

mysavings_account = SavingsBankAccount(20000)
mysavings_account.withdraw(25000)
mysavings_account.deposit(7000)
print(mysavings_account.balance)


