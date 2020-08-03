
print([x for x in range(2, 201) if all(x % y != 0 for y in range(2, x))])
