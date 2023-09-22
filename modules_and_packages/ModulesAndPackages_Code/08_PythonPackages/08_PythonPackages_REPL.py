# Example 01
import pkg.mod1, pkg.mod2
pkg.mod1.load_data()

x = pkg.mod2.Location()
print(x)

# Example 02
from pkg.mod1 import load_data
load_data()

# Example 03
from pkg.mod2 import Location as Primary
y = Primary()
print(y)

# Example 04
from pkg import mod1
mod1.load_data

from pkg import mod2 as foo
foo.clean_data()

# Example 05
import pkg
pkg

pkg.mod1

pkg.mod2.Location

pkg.mod1.load_data()
