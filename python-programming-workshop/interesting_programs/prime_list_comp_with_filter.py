

print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 201))))
