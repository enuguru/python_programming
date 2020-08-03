
mz = (lambda a = 'Wolfgangus', b = ' Theophilus', c = ' Mozart': a + b + c)
print(mz())
print(mz('Wolfgang', ' Amadeus'))

def writer():
  title = 'Sir'
  name = (lambda x:title + ' ' + x)
  return name

who = writer()
print(who('Arthur Ignatius Conan Doyle'))
