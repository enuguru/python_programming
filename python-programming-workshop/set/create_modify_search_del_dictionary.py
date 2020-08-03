
mydictionary = { }
mydictionary["salary"] = 1000000
mydictionary["age"] = 45
print(mydictionary)

dictone = {"name":"Aprameya","salary":1000000}
print(dictone)

newdict = dict([("Cat",5),("Dogs",3)])
print(newdict)

dictone["age"] = 16
print(dictone)

dictone["age"] = 15
print(dictone)

if "age" in dictone:
    print("age is present in the dictionary")
else:
    print("age is not present in the dictionary")

del(dictone["age"])
print(dictone)
