
# in your string "apple" the unique characters are
# a, l and e. so you can print them. right?
 
teststr = "apple"
dictstr = {}
for i in range(0, len(teststr)):
    print(str(i) + " " + teststr[i])
    #dictstr[i] = teststr[i]
    dictstr[teststr[i]] = i
print(dictstr)
print("number of unique characters in the string is %d" %len(dictstr))
