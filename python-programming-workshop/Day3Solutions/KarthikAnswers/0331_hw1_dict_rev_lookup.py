
# the program is fine neat, no comments karthick

temp_dict = {"a":1, "b":2, "c":3, "d":1}
print(temp_dict)
print(temp_dict.keys())

print("keys in temp dict:")
for keystr in temp_dict:
    print(keystr)

print("values in temp dict:")
for valuestr in temp_dict.values():
    print(valuestr)

print("Reverse lookup for keys in temp dict (for value 1):")
lookupvalue = 1
for keystr in temp_dict:
    if temp_dict[keystr] == lookupvalue:
        print(keystr)
