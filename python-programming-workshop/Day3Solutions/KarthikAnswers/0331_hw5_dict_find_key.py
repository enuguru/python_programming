
# your solution is fine and works good
# just as a reference in passing i want to 
# say, there is a syntax like the one given below
# here name is the key, bankbalance is the value

# for name, bankbalance in mydict.items():
#    if bankbalance == given_balance:
#        print name

# but your solution just works fine no issues

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
