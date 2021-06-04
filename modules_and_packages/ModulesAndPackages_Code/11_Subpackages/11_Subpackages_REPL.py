# Example 01
import pkg.sub_pkg1.mod1
pkg.sub_pkg1.mod1.load_data()

from pkg.sub_pkg1 import mod2
dir()
mod2.clean_data()

from pkg.sub_pkg2.mod3 import merge_data
merge_data()

from pkg.sub_pkg2.mod4 import Winner as Result
x = Result()
x

# Example 02
from pkg.sub_pkg2 import mod3

mod3.load_data()

# Example 03
from pkg.sub_pkg2 import mod3

dir()
