
# Read a collection of words entered by the user. display
# each word entered by the user only once, in the same order
# that the words are entered. use a list

newset = set()

for count in range(5):
    word = input("Give a word")
    newset.add(word)
print(newset)

newlist= []

for count in range(5):
    word = input("Give a word")
    newlist.append(word)
newset = set(newlist)
print(newset)
