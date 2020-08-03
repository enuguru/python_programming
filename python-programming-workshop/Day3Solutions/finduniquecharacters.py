

inputstring = input("Enter a string:    ");

uniquecharacters = { }
for ch in inputstring:
    uniquecharacters[ch] = True


print("The input string contained", len(uniquecharacters), "unique character(s).")
print(" and the characters are")
for key in uniquecharacters:
    print(key," ")
