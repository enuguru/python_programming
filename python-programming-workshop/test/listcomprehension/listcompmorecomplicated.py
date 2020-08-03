
result = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(result)
