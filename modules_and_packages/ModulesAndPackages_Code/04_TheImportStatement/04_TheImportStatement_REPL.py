# Example 01
import mod
mod

# Example 02
a
s
printy

# Example 03
mod.a
mod.s
mod.printy('Hello')

# Example 04
from mod import s, printy
s
printy('Hello')

# Example 05
a = ['abc', 'def', 'ghi']
a

from mod import a
a

# Example 06
from mod import *
s
a
printy
Classy

# Example 07
a = ['abc', 'def', 'ghi']
s = 'Hello There!'

from mod import s as string, a as alist
a
s

string
alist

# Example 08
import mod as my_module
my_module.a

my_module.s

# Example 09
def importer():
    from mod import printy
    printy('Hello Everyone')

mod
printy

importer()

# Example 10
def importer2():
    from mod import *

# Example 11
try:
    # Non-existent module
    import foo
except ImportError:
    print('Module not found')

try:
    # Existing module, but non-existent object
    from mod import bar
except ImportError:
    print('Object not found in module')

