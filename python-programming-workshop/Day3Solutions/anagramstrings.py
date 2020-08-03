
def characterCounts(s):
    charcounts = { }
    for ch in s:
        if ch in charcounts:
            charcounts[ch] = charcounts[ch] + 1
        else:
            charcounts[ch] = 1
    return charcounts

inputone = input("Enter the first string: ")
inputtwo = input("Enter the second string: ")

countsone = characterCounts(inputone)
countstwo = characterCounts(inputtwo)


if countsone == countstwo:
    print("These strings are anagrams of each other ")
else:
    print("These strings are not anagrams of each other ")
