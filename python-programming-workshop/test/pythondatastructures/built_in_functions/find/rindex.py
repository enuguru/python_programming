
#Python program that uses string index

value = "abc def pqr abc fgh"

#Use index method.
i = value.index("def")
print(i)

# This causes an exception.
b = value.rindex("pqr",0,len(value))
print(b)
