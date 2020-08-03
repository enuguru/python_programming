

import time

print(time.time())

# Compute absolute value with abs.
a = -1
i = 0
while i < 10000000:
    b = abs(a)
    i += 1

print(time.time())

# Compute absolute value with if-statement.
a = -1
i = 0
while i < 10000000:
    if a < 0:
        b = -a
    else:
        b = a
    i += 1

print(time.time())
