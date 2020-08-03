

#Python that benchmarks if, tuple

import time

print(time.time())

# Version that uses tuple.
v = 0
i = 0
x = 2

while i < 10000000:
    if x in (1, 2, 3):
        v += 1
    i += 1

print(time.time())

# Version that uses if-elif.
v = 0
i = 0
while i < 10000000:
    if x == 1:
        v += 1
    elif x == 2:
        v += 1
    elif x == 3:
        v += 1
    i += 1

print(time.time())
