
#regex_pattern = r"\D+"	# Do not delete 'r'

import re
s = input()
args = re.split("[.,]",s)
for x in args:
    if x:
        print(x)

print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

