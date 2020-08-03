
#Python that gets future dates, range

from datetime import date, timedelta

# Start with today.
start = date.today()
print(start)

# Add 1 to 10 days and get future days.
for add in range(1, 10):
    future = start + timedelta(days=add)
    print(future)
