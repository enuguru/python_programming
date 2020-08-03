

#Python program that uses timedelta

# this is beautiful - this is a great example of dynamic typing or duck typing

from datetime import timedelta

# This represents 1 day.
a = timedelta(days=1)

# Represents 1 hour.
b = timedelta(hours=1)

# Subtract 1 hour from 1 day.
c = a - b
print(c)
