
a = 2
b = 7
generator = (i*i for i in range(a, b))

for i in generator:
    print(i)
