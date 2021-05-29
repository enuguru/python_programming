
import re

regex_pattern = r"[,.-]"

print(re.split(regex_pattern,input()))

#345,567.78,45

#345567
#78
#45

