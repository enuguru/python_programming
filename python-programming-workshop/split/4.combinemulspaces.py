
#Collapse multiple spaces into one

mystring = 'collapse    these       spaces'

newstring = mystring.split()
print(newstring)
mycollapsedstring = ' '.join(mystring.split())

print(mycollapsedstring.split(' '))
['collapse', 'these', 'spaces']
