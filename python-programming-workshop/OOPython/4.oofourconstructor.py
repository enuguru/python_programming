

#dunder method - magic method
class BankBalance:
    def __init__(self, acctype, amount):    # Constructor of the class
        self.acctype = acctype
        self.amount = amount

a = BankBalance('savings', 10000)

print(a.acctype)
print(a.amount)
