
#Python program that gets tomorrow

from datetime import date
from datetime import timedelta

def tomorrow():
    # Add one day delta.
    return date.today() + timedelta(days=1)

print(date.today())
print(tomorrow())
