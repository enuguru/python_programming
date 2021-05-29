
a = ["hello" "friends"]
print("The builtin functions of the list are")
print(dir(a),end="  ")
print("\n\n")

class a:
    pass

print("The builtin functions of the class are")
print(dir(a),end="  ")
print("\n\n")

x = 20
y = 30
a = {x:"hello", y:"friends"}
print("The builtin functions of the dictionary are")
print(dir(a),end="  ")
print("\n\n")

a = {"hello", "friends"}
print("The builtin functions of the set are")
print(dir(a),end="  ")
print("\n\n")

a = ("hello", "friends")
print("The builtin functions of the tuple are")
print(dir(a),end="  ")
print("\n\n")

import builtins
print("The builtin functions in python are")
print(dir(builtins),end="  ")
print("\n\n")

import types
builtin_functions = [obj for name, obj in vars(builtins).items()
                     if isinstance(obj, types.BuiltinFunctionType)]
print("The builtin functions in python are\n")
print(dir(builtin_functions),end="  ")
print("\n\n")

import collections
print("The builtin collection functions in python are\n")
print(dir(collections),end="  ")
print("\n\n")

import itertools
print("The builtin itertools functions in python are\n")
print(dir(collections),end="  ")
print("\n\n")

import functools
print("The builtin functools functions in python are\n")
print(dir(functools),end="  ")
print("\n\n")

import click
print("The builtin click functions in python are\n")
for e in dir(click):
    print(e,end="  ")
print("\n\n")



import itertools
print("The builtin itertools functions in python are\n")
for e in dir(itertools):
    print(e,end="  ")
print("\n\n")


