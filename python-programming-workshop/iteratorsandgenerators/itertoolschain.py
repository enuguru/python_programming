
import itertools

values1 = [1, 2, 3, 4]
values2 = [5, 6, 7, 8]
values3 = [9, 10]

# Chain three lists into one iterable.
result = itertools.chain(values1, values2, values3)
print(list(result))
