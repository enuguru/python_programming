
#Python program that sorts date list

from datetime import date, timedelta

# Create a list of dates.
values = []
values.append(date.today() + timedelta(days=300))
values.append(date.today() + timedelta(days=2))
values.append(date.today() + timedelta(days=1))
values.append(date.today() + timedelta(days=20))

# Sort the list.
values.sort()

# Display.
for d in values:
   print(d)
