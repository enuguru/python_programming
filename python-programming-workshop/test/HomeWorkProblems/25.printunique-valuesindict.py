
## python program to print unique (nonduplicate) values in a dictionary ##

nondup = set()
newdictionary = {"one":23,"two":34,"three":23}
print(" Datas in dictionary : ", newdictionary)

for k,v in newdictionary.items():
    nondup.add(v)

print(" Non duplicate (unique) values in the dictionary are : ",nondup)
