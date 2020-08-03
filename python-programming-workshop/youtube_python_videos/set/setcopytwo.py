

## Shallow copy of a set using = operator

numbers = {1, 2, 3, 4}

# Shallow copy
new_numbers = set(numbers)

new_numbers.add('5')

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
