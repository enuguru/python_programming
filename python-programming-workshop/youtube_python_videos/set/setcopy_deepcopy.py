

## Deep Copy

## If you modify the numbers set, the new_numbers set is also modified. This is called Deep Copy

numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add('5')

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
