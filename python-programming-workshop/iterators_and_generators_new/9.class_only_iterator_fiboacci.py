
class generate_fibonacci:

    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value

    def __iter__(self):
        return self
    
f = generate_fibonacci()
print()

for i in range(20):
    print(next(f),end= " ")
print("\n\n")
