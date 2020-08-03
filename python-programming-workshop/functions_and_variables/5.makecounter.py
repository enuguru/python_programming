
count = 67
def make_counter():
    count = 10
    def counter():
        #count = 90
        nonlocal count
        count += 1
        return count
    return counter()

print(make_counter())
p = make_counter()
print(p)
