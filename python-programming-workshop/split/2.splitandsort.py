# Program to sort alphabetically the words form a string provided by the user

# take input from the user
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()
print(words)

# sort the list
words.sort()
print(words)

# display the sorted words
#for word in words:
#   print(word)
