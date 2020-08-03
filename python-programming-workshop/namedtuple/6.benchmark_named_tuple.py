
#Python program that benchmarks namedtuple, tuple

import collections
import time

# The namedtuple instance.
Animal = collections.namedtuple("Animal", ["size", "color"])

print(time.time())

# Version 1: create namedtuple.
i = 0
while i < 10000000:
    a = Animal(100, "blue")
    if a[0] != 100:
       raise Exception()
    i += 1

print(time.time())

# Version 2: create tuple.
i = 0
while i < 10000000:
    a = (100, "blue")
    if a[0] != 100:
       raise Exception()
    i += 1

print(time.time())
