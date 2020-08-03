

# please solve the above problem by using a dictionary

newset = set()

for count in range(3):
    word = input("Give a word")
    newset.add(word)
print(newset)

newdict= {}
currentset = set()

for count in range(3):
    word = input("Give a word")
    newdict[count] = word
    currentset.add(word)
print(currentset)
