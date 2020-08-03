
#assume we want to create a list of squares.

# You can either use loops:
squares = []

for x in range(10):
    squares.append(x**2)
 
print(squares)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Or you can use list comprehensions to get the same result:
squares = [x**2 for x in range(10)]

print(squares)

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
