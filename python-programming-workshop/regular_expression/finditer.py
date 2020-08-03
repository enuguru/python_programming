

# Finditer. 

# Unlike re.findall, which returns strings, finditer returns matches. For each match, we call 
# methods like start() or end(). And we can access the value of the match with group().

# Python program that uses finditer

import re

value = "123 456 7890"

# Loop over all matches found.
for m in re.finditer("\d+", value):
    print(m.group(0))
    print("start index:", m.start())

