# Pythonic solution uses the power of itertools.groupby

# 333
# 21
# 2 [2], 1 [1]
# 7 7 [7]  1 11 21 1211 111221 312211 

import itertools

def lookandsaypythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''. join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

for val in range(1,11):
    number = lookandsaypythonic(val)
    print(number)

#  33322445

# 3322

#  3 [3,3,3] 2 [2,2] 4 [4,4] 5 [5]
