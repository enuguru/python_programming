# Example 01
dir()

spam = [1, 2, 3, 4, 5]
spam

dir()

class Extraclassy():
    pass

x = Extraclassy()
dir()

# Example 02
dir()

import mod
dir()

mod.s
mod.printy([1, 2, 3])

from mod import a, Classy
dir()

a
y = Classy()
y

from mod import s as string
dir()

s
string

# Example 03
import mod
dir()

dir(mod)

dir()

from mod import *
dir()
