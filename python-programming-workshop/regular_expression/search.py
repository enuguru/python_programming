
#Search. This method is different from match. Both apply a pattern. But search attempts this 
#at all possible starting points in the string. Match just tries the first starting point.

#So:Search scans through the input string and tries to match at any location. In this 
#example, search succeeds but match fails.


#Python program that uses search

import re

# Input.
value = "voorheesville"

m = re.search("(vi.*)", value)
if m:
    # This is reached.
    print("search:", m.group(1))

m = re.match("(vi.*)", value)
if m:
    # This is not reached.
    print("match:", m.group(1))

#Output

#search: ville

#Pattern details

#Pattern: (vi.*)

#vi       The lowercase letters v and i together.
#.*       Zero or more characters of any type.
