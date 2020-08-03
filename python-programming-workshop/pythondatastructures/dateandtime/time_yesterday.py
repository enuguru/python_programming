

#Python program that returns yesterday

from datetime import date
from datetime import timedelta

def yesterday():
    # Get today.
    today = date.today()
    # Subtract timedelta of 1 day.
    yesterday = today - timedelta(days=1)
    return yesterday

print(date.today())
print(yesterday())
