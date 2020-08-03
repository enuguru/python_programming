
# good solution karthick, can you try this without using set

#remove duplicates from a sequence of numbers given as input using set

user_input = input()
list_numbers = list(map(int, user_input.split(',')))

print(list_numbers)

set_numbers = set(list_numbers)
print("after removing the duplicates:")
print(set_numbers)


