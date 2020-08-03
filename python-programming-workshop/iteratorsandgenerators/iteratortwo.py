
class Naturals():
    def __init__(self):
        self.current = 0

def __next__(self):
    result = self.current
    self.current += 1
    return result

def __iter__(self):
    return self

nats = Naturals()
print(nats)
nats_iter = iter(nats)
print(next(nats_iter))
#next(nats_iter)
#next(nats_iter)
