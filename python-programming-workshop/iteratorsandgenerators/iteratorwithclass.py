
class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1
        print("The __init__ constructor is called")

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr < 10:
            self.value = self.curr
            self.curr += self.prev
            self.prev = self.value
            yield self.value

f = fib()
for i in f:
    print(i)
#print(f)
#print(next(f))
#print(next(f))
#print(next(f))
