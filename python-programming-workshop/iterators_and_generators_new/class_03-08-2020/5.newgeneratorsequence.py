
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# Create the generator, notice no output appears
c = countdown(9)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


c = countdown(9)
for num in range(9,3,-1):
    print(next(c))
#for num in range:
#    print(c)


# Run to first yield and emit a value
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
#print(next(c))
