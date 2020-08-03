

#Python program that benchmarks generator

import time

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(time.time())

# Version 1: generator.
i = 0
while i < 1000000:
    double = list(x * 2 for x in data)
    i += 1

print(time.time())

# Version 2: list comprehension.
i = 0
while i < 1000000:
    double = [x * 2 for x in data]
    i += 1

print(time.time())
