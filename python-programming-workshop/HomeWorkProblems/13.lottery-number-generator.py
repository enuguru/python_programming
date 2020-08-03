
# compute random and distinct numbers for a lottery ticket.
# (clue: what we I am asking is, generate unique random numbers
# for a lottery ticket)

import random
print(sorted(random.sample(range(1,10000000), 10)))