

#Python program that benchmarks sorted, reversed

import time

data = ["carrot", "apple", "peach", "nectarine"]

print(time.time())

# Version 1: use sort and reverse.
i = 0
while i < 1000000:
    v = 0
    data.sort()
    for element in data:
        v += 1
    data.reverse()
    for element in data:
        v += 1
    i += 1

print(time.time())

# Version 2: use sorted and reversed.
i = 0
while i < 1000000:
    v = 0
    for element in sorted(data):
        v += 1
    for element in reversed(data):
        v += 1
    i += 1

print(time.time())
