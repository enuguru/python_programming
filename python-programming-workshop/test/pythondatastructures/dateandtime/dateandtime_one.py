


#Python program that uses strptime

from datetime import datetime

# Input string.
s = "April 14, 2015"

# Use strptime.
d = datetime.strptime(s, "%B %d, %Y")
print(d)
