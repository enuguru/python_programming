
squares = []

# 1st method

for x in range(10):
    squares.append(x**2)
print(squares)


# 2nd method

squarestwo = [x**2 for x in range(10)]
print(squarestwo)


# 3rd method

squaresone = list(map(lambda x: x**2, range(10)))
print(squaresone)




