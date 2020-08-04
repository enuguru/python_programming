
class generate_fiboacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a+self.b


f = generate_fiboacci()
p=f.__iter__()
for i in range(20):
    print(next(p),end=" ")
print()


f = iter(generate_fiboacci())
for i in range(20):
    print(next(f),end=" ")
print()
