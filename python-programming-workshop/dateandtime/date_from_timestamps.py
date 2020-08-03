

#Python program that gets timestamps, converts to dates

from os import path
from datetime import date

# Get access, modification, and creation time.
a = path.getatime("/enable1.txt")
m = path.getmtime("/enable1.txt")
c = path.getctime("/enable1.txt")

# Display the times.
print(a, m, c)

# Convert timestamps to dates.
a2 = date.fromtimestamp(a)
m2 = date.fromtimestamp(m)
c2 = date.fromtimestamp(c)
print(a2, m2, c2)
