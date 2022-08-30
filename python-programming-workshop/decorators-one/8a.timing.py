
def new_function():
    new_list = []
    for num in (range(0, 1000000)):
        new_list.append(num)
    print("\nSum of all the numbers: " + str((sum(new_list))))

print(new_function())
