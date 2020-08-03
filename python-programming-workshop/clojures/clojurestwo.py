def make_counter():
    next_value = 0
    def return_next_value():
        nonlocal next_value
        val = next_value
        next_value += 1
        return val
    return return_next_value

my_first_counter = make_counter()
my_second_counter = make_counter()
print(my_first_counter())
print(my_second_counter())
print(my_first_counter())
print(my_second_counter())
print(my_first_counter())
print(my_second_counter())
