

import itertools

# Generate count from 0 to infinity, with step 2.
result = itertools.count(0, 2)

# Display until value 10.
for value in result:
    print(value)
    if value >= 10: break
