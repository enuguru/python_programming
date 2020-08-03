
balance = 0

def deposit(amount):
    global balance
    balance += amount
    #return balance

def withdraw(amount):
    global balance
    balance -= amount
    #return balance

deposit(1000000)
print(balance)
withdraw(100000)
print(balance)
