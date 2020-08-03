
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
b = make_account()
print(deposit(a, 1000000))
print(deposit(b, 50000))
print(withdraw(b, 1000))
print(withdraw(a, 2000))
