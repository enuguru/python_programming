
demolist = ["life", 42, "the universe", 6, "and", 9]
print("demolist = ",demolist)
demolist.append("everything")
print("after 'everything' was appended demolist is now:")
demolist.insert(1,7)
print(demolist)
demolist.remove(6)
demolist.pop(1)
demolist.insert(3,17)
demolist.pop()
print(demolist)
print("len(demolist) =", len(demolist))
print("demolist.index(42) =", demolist.index(42))
print("demolist[1] =", demolist[1])
 
# Next we will loop through the list
for c in range(len(demolist)):
    print("demolist[", c, "] =", demolist[c])
 
del demolist[2]
print("After 'the universe' was removed demolist is now:")
print(demolist)
if "life" in demolist:
    print("'life' was found in demolist")
else:
    print("'life' was not found in demolist")
 
if "amoeba" in demolist:
    print("'amoeba' was found in demolist")
 
if "amoeba" not in demolist:
    print("'amoeba' was not found in demolist")
 
another_list = [42,7,0,123]
print("This is another_list and it contains")
print(another_list)
another_list.sort()
print("The sorted of another_list is", another_list)
