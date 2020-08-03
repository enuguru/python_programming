

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

dictone = { x:100, x[1]:105 }
print(dictone)
