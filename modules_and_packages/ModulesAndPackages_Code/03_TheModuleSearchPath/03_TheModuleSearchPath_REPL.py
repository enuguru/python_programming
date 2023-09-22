# Example 01
import mod
print(mod.a)

print(mod.s)

# Example 02
import sys
print(sys.path,"\n")

# Example 03
sys.path.append(r'/Users/karth/python_programming/modules_and_packages/ModulesAndPackages_Code') #change this to be the path on your own computer
sys.path
import mod

print(mod.s)

# Example 04
import mod
print(mod.__file__)

import re
print(re.__file__)
