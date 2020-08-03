
#!/usr/bin/env python

import re

shakes = open("listone", "r")

for line in shakes:
#   if re.match("(.*)(L|l)ove(.*)", line):
        print(line)

