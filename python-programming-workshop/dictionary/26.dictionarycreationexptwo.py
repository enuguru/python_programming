
mydict = {'Lemonade': ["1", "45", "87"], 'Coke': ["23", "9", "23"], 'Water': ["98", "127"]}
for imp in mydict:
  print(imp)
  print(mydict[imp])

for key,val in mydict.items():
  print(key)
  print(val)

x = mydict.keys()
y = mydict.values()

print(x)
print(y)

print(mydict.keys())
print(mydict.values())

x = (23,34)
y = ((23,56),(34,"Jayashree"))
print(y)

karthik = { y:"BadriNarayanan" }
print(karthik)
print(karthik[((23, 56), (34, 'Jayashree'))])
print(karthik[y])

guru = { (3,4):"BadriNarayanan"}
print(guru)

dictone = { x:100, x[1]:105 }
print(dictone.keys())
print(dictone.values())
print(dictone)
dicttwo = {y:100} # this will product "TypeError: unhashable type: 'list'"
# this error comes because the key should be immutable. This means a list
#cannot be used as the key. Comment the above line to remove this error (line number 28)
dicttwo = {y[1]:100}
print(dicttwo)


myset =  { 34, "guru", "karthik" }
print(myset)
