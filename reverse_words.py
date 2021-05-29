# how to give the input ?
# give a single sentence like "hello how are you doing" ? as input

newstring = input()

## splitting the string on space
words = newstring.split()

## reversing the words using reversed() function
words = list(reversed(words))

## joining the words and printing
print(" ".join(words))
