

#Python program that times, while, for-range loop

import time

print(time.time())

# Version 1: while-loop.
c = 0
i = 0
while i < 10000000:
    c += i
    i += 1

print(time.time())

# Version 2: for-range loop.
c2 = 0
for y in range(0, 10000000):
    c2 += y

print(time.time())
