

from datetime import *

def yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday

print(date.today())
print(yesterday())
