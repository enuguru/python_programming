
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

a = 2
b = 7
generator = squares(a, b)
for i in generator:
    print(i)
print(generator)
