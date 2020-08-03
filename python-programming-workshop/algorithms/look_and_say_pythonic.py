
# Pythonic solutjon uses the power of itertools.groupby

import itertools

def lookandsaypythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''. join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

for val in range(1,11):
    number = lookandsaypythonic(val)
    print(number)
