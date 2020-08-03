

# write a program that creates a dictionary with numbers
# as values and print the top 3 highest values in the dictionary

newlist = []
newdictionary = {"one":23,"two":34,"three":29,"Four":45,"Five":56}
print(" Datas in dictionary : ", newdictionary)

for k,v in newdictionary.items():
    newlist.append(v)
print(newlist)

ascendinglist = sorted(newlist,reverse=True)
for count in range(3):
    print(ascendinglist[count])
