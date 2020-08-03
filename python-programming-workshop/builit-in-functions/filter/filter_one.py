
numbers = [10, 20, 0, 0, 30, 40, -10]

# Filter out numbers equal to or less than zero.
result = list(filter(lambda n: n > 0, numbers))
print(result)
