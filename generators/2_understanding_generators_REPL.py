# Example 01
import gen1
print(gen1.infinite_sequence())

# Example 02 - inifinite sequence version 1
import gen1
infinite = gen1.infinite_sequence()
type(infinite)
next(infinite)
next(infinite)
next(infinite)
next(infinite)
next(infinite)

# Example 03 - inifinite sequence version 2
import gen1
infinite = gen1.infinite_sequence()
next(infinite)
next(infinite)
next(infinite)

# Example 04 - finite sequence
import gen1
finite = gen1.finite_sequence()
next(finite)
next(finite)
next(finite)
next(finite)

# Example 05 - list comprehension vs generator expression syntax
import gen1
gen1.nums_squared_lc
gen1.nums_squared_gc

# Example 06 - comparing performance of  list comprehension vs generator expression
import sys
nums_squared_lc = [num**2 for num in range(100000)]
nums_squared_gc = (nums**2 for num in range(100000))
sys.getsizeof(nums_squared_lc)
sys.getsizeof(nums_squared_gc)

import cProfile
cProfile.run('sum([i*2 for i in range(100000)])')

cProfile.run(('sum((i*2 for i in range(100000)))'))
