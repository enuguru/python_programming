
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# Create the generator, notice no output appears
c = countdown(9)
print(c)
print(next(c))
input("Press Enter to continue...")

print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
print(next(c))
input("Press Enter to continue...")
