

#No arguments. Split() can be called with no argument. In this case, split() uses spaces as the delimiter. Please notice that one or more spaces are treated the same.

#Python program that uses split, no arguments

# Input string.
# ... Irregular number of spaces between words.
s = "One two   three"

# Call split with no arguments.
words = s.split()

# Display results.
for word in words:
    print(word)
