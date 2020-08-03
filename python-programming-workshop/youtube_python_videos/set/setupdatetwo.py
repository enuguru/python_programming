

## Adding elements of String and Dictionary to set

# Update With String
string_alphabet = 'abc'
numbers_set = {1, 2}

numbers_set.update(string_alphabet)

print('numbers_set =',numbers_set)
print('string_alphabet =',string_alphabet)

# Update With Dictionary
info_dictionary = {'key': 1, 2 : 'lock'}
numbers_set = {'a', 'b'}

numbers_set.update(info_dictionary)
print('numbers_set =',numbers_set)
