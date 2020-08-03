
# Compute the number of unique characters in a string
# using a dictionary (clue: unique characters means you have
# count the characters and print the characters that are unique)

newset = set()
newstring = "phenomenal"

for char in newstring:
    newset.add(char)

newset = sorted(newset)
print(newset)
