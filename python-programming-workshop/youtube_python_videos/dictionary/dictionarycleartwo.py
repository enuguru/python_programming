

d = {1: "one", 2: "two"}
d1 = d
d.clear()
print('Removing items using clear()')
print('d =', d)
print('d1 =', d1)

d = {1: "one", 2: "two"}
d1 = d
d = {}
print('Removing items by assigning {}')
print('d =', d)
print('d1 =', d1)
