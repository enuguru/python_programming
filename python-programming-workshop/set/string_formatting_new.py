
mytuple = (56,67,45)

x = 16 
name = "Aprameya"

print("My name is %s and my age is %d years"%(name,x))
print("My name is {} and my age is {} years".format(name,x))

if x in mytuple:
    print("The number %d is present in mytuple"%x)
else:
    print("The number %d is not present in mytuple"%x)

if x in mytuple:
    print("The number {} is present in mytuple".format(x))
else:
    print("The number {} is not present in mytuple".format(x))
