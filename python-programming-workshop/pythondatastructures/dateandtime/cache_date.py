

#Cache. Getting the date, as with date.today(), is slow. This call must access the operating 
#system. An easy way to optimize this is to cache dates.

#Loop 1: This loop access date.today() once on each iteration through the loop. It runs much slower.

#Loop 2: The date.today() call is cached in a variable before the loop runs. This makes each 
#iteration much faster. We hoist the call.

#Also: The logic checks the year of the date. This can be changed for the current year.

#Python that caches date

import time
from datetime import date

# Time 1.
print(time.time())

# Accesses today repeatedly.
i = 0
while i < 100000:
    t = date.today()
    if t.year != 2015:
        raise Exception()
    i += 1

# Time 2.
print(time.time())

# Accesses today once.
i = 0
t = date.today()
while i < 100000:
    if t.year != 2015:
        raise Exception()
    i += 1

# Time 3.
print(time.time())
