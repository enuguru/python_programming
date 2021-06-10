

import itertools
mod5=[n for n in range(101)]
result=itertools.filterfalse(lambda e: (e%5)!=0,mod5)
for i in result:
    print(i)
