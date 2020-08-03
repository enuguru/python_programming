
#if you want to chomp the items one at a time:

mystring = "theres coffee in that nebula"

mytuple = mystring.partition(" ")

print(type(mytuple))
#<type 'tuple'>

print(mytuple)
#('theres', ' ', 'coffee in that nebula')

print(mytuple[0])
#theres

print(mytuple[2])
#coffee in that nebula
