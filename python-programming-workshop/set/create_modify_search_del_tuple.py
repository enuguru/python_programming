
# tuple values once given are immutable

mytuple = (45,35)
print(mytuple)

newtuple = tuple([39,99])
print(newtuple)

myset = set([34,45])
print(myset)

newset = {34,49}
print(newset)

print(mytuple)

x = 45
if x in mytuple:
    print("The number %d is present in mytuple"%x)
else:
    print("The number %d is not present in mytuple"%x)


if x in mytuple:
    print("The number {} is present in mytuple".format(x))
else:
    print("The number {} is not present in mytuple".format(x))
