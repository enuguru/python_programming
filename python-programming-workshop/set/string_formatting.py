
mytuple = (56,67,45)
x = 45
if x in mytuple:
    print("The number %d is present in mytuple"%x)
else:
    print("The number %d is not present in mytuple"%x)


if x in mytuple:
    print("The number {} is present in mytuple".format(x))
else:
    print("The number {} is not present in mytuple".format(x))

births = 9
print("If there was a birth every 7 seconds, there would be: %d births" %births)

births = 9
print("If there was a birth every 7 seconds, there would be: {} births".format(births))
