
class generate_fiboacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a+self.b
        
f = iter(generate_fiboacci())
for i in range(20):
    print(next(f),end=" ")
print()
