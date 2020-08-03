

import random

# A while-true loop.
while True:
    n = random.randint(0, 100)
    print(n)
    # Break on even random number.
    if n % 2 == 0:
        break
