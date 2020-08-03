
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter()

p = make_counter()
print(p)
